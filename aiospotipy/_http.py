import logging
import asyncio
import aiohttp
import json

log = logging.getLogger(__name__)
GET = "GET"
POST = "POST"
DELETE = "DELETE"
PUT = "PUT"


async def async_none():
    return None


def get_id(_type, _id):
    fields = _id.split(':')
    if len(fields) >= 3:
        if _type != fields[-2]:
            log.debug('expected id of type %s but found type %s %s', _type, fields[-2], _id)
        return fields[-1]
    fields = _id.split('/')
    if len(fields) >= 3:
        itype = fields[-2]
        if _type != itype:
            log.debug('expected id of type %s but found type %s %s', _type, itype, _id)
        return fields[-1]
    return _id


def get_uri(_type, _id):
    return 'spotify:' + _type + ":" + get_id(_type, _id)


class SpotifyException(Exception):
    def __init__(self, http_status, code, msg, headers=None):
        self.http_status = http_status
        self.code = code
        self.msg = msg
        # `headers` is used to support `Retry-After` in the event of a
        # 429 status code.
        if headers is None:
            headers = {}
        self.headers = headers

    def __str__(self):
        return 'http status: {0}, code:{1} - {2}'.format(
            self.http_status, self.code, self.msg)


class Route:
    BASE = 'https://api.spotify.com/v1'

    def __init__(self, method, path, payload=None, **parameters):
        self.payload = payload
        self.path = path
        self.method = method
        self.params = {}
        for key, value in parameters.items():
            if value is None:
                continue
            self.params[key] = value
        self.url = (self.BASE + self.path)


class HTTPClient:
    def __init__(self, auth=None, client_credentials_manager=None, connector=None, *, proxy=None, loop=None,
                 timeout=30):
        self.auth = auth
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.client_credentials_manager = client_credentials_manager
        self.connector = connector
        self.timeout = timeout
        self.proxy = proxy

    async def auth_headers(self):
        token = self.client_credentials_manager.get_access_token() if not self.auth else self.auth
        return {'Authorization': f'Bearer {token}'}

    async def request(self, route, **kwargs) -> dict:
        status_code, text, headers = None, None, None
        method = route.method
        url = route.url
        payload = route.payload
        args = dict(params=route.params)
        args["timeout"] = self.timeout
        request_field = kwargs.get('request_field', None)
        _headers = await self.auth_headers()
        _headers['Content-Type'] = 'application/json'
        if payload:
            args["data"] = json.dumps(payload)
        async with aiohttp.ClientSession() as session:
            if method == GET:
                async with session.get(url, headers=_headers, proxy=self.proxy, **args) as r:
                    text = await r.text()
                    status_code = r.status
                    headers = r.headers

            elif method == POST:
                async with session.post(url, headers=headers, verify=True,
                                        proxy=self.proxy, **args) as r:
                    text = await r.text()
                    status_code = r.status
                    headers = r.headers

            elif method == DELETE:
                async with session.delete(url, **args) as r:
                    text = await r.text()
                    status_code = r.status
                    headers = r.headers

            elif method == PUT:
                async with session.put(url, **args) as r:
                    text = await r.text()
                    status_code = r.status
                    headers = r.headers
            await session.close()

        if not 200 <= status_code and not status_code < 300:
            if text and len(text) > 0 and text != 'null':
                raise SpotifyException(status_code,
                                       -1, '%s:\n %s' % (url, json.loads(text)['error']['message']),
                                       headers=headers)
            else:
                raise SpotifyException(status_code, -1, '%s:\n %s' % (url, 'error'), headers=headers)
        if text and len(text) > 0 and text != 'null':
            _json = json.loads(text)
            if request_field and request_field in _json.keys():
                return _json[request_field]
            return _json
        else:
            return {}

    async def next(self, result):
        if result['next']:
            r = Route(GET, result['next'])

            return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)
        else:
            return async_none()

    async def previous(self, result):
        if result['previous']:
            r = Route(GET, result['previous'])

            return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)
        else:
            return async_none()

    async def track(self, track_id):
        trid = get_id('track', track_id)
        r = Route(GET, '/tracks/' + trid)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def tracks(self, tracks, market):
        tlist = [get_id('track', t) for t in tracks]
        r = Route(GET, '/tracks/?ids=' + ','.join(tlist), market=market)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def artist(self, artist_id):
        trid = get_id('artist', artist_id)
        r = Route(GET, '/artists/' + trid)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def artists(self, artists):
        tlist = [get_id('artist', a) for a in artists]
        r = Route(GET, '/artists/?ids=' + ','.join(tlist))

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def artist_albums(self, artist_id, album_type, country, limit, offset):
        trid = get_id('artist', artist_id)
        r = Route(GET, f'/artists/{trid}/albums',
                  album_type=album_type, country=country, limit=limit, offset=offset)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def artist_top_tracks(self, artist_id, country):
        trid = get_id('artist', artist_id)
        r = Route(GET, f'/artists/{trid}/top-tracks', country=country)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def artist_related_artists(self, artist_id):
        trid = get_id('artist', artist_id)
        r = Route(GET, f'/artists/{trid}/related-artists')

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def album(self, album_id):
        trid = get_id('album', album_id)
        r = Route(GET, 'albums/' + trid)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def album_tracks(self, album_id, limit, offset):
        trid = get_id('album', album_id)
        r = Route(GET,
                  f'albums/{trid}/tracks/',
                  limit=limit, offset=offset)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def albums(self, albums):
        tlist = [get_id('album', a) for a in albums]
        r = Route(GET, 'albums/?ids=' + ','.join(tlist))
        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def search(self, q, limit, offset, _type, market):
        r = Route(GET,
                  '/search/',
                  q=q, limit=limit, offset=offset, type=_type, market=market)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def search_artist(self, q, limit, offset, market):
        r = Route(GET,
                  '/search/',
                  q=q, limit=limit, offset=offset, type="artist", market=market)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def search_album(self, q, limit, offset, market):
        r = Route(GET,
                  '/search/',
                  q=q, limit=limit, offset=offset, type="album", market=market)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def search_track(self, q, limit, offset, market):
        r = Route(GET,
                  '/search/',
                  q=q, limit=limit, offset=offset, type="track", market=market)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def search_playlist(self, q, limit, offset, market):
        r = Route(GET,
                  '/search/',
                  q=q, limit=limit, offset=offset, type="playlist", market=market)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def user(self, user):
        r = Route(GET, '/users/' + user)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def user_playlists(self, user, limit, offset):
        r = Route(GET,
                  f"/users/{user}/playlists",
                  limit=limit, offset=offset)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def user_playlist(self, user, playlist_id, fields):
        if not playlist_id:
            r = Route(GET, f"/users/{user}/starred", fields=fields)
        else:
            plid = get_id('playlist', playlist_id)
            r = Route(GET,
                      f"/users/{user}/playlists/{plid}",
                      fields=fields)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def get_playlist_tracks(self, user, playlist_id, fields, limit, offset, market):
        plid = get_id('playlist', playlist_id)
        r = Route(GET,
                  f"/users/{user}/playlists/{plid}/tracks",
                  limit=limit, offset=offset, fields=fields, market=market)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def playlist_create(self, user, name, public):
        data = {'name': name, 'public': public}
        r = Route(POST,
                  f"/users/{user}/playlists",
                  payload=data)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def playlist_change_details(self, user, playlist_id, name, public, collaborative):
        data = {}

        if isinstance(name, str):
            data['name'] = name
        if isinstance(public, bool):
            data['public'] = public
        if isinstance(collaborative, bool):
            data['collaborative'] = collaborative
        r = Route(PUT,
                  f"/users/{user}/playlists/{playlist_id}",
                  payload=data)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def unfollow_playlist(self, user, playlist_id):
        r = Route(DELETE,
                  f"/users/{user}/playlists/{playlist_id}/followers")

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def playlist_add_tracks(self, user, _playlist_id, tracks, position):
        playlist_id = get_id('playlist', _playlist_id)
        ftracks = [get_uri('track', tid) for tid in tracks]
        r = Route(POST,
                  f"/users/{user}/playlists/{playlist_id}/tracks",
                  payload=ftracks, position=position)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def playlist_replace_tracks(self, user, _playlist_id, _tracks):
        playlist_id = get_id('playlist', _playlist_id)
        tracks = [get_uri('track', tid) for tid in _tracks]
        payload = {"uris": tracks}
        r = Route(PUT,
                  f"/users/{user}/playlists/{playlist_id}/tracks",
                  payload=payload)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def playlist_reorder_tracks(self, user, _playlist_id, range_start, insert_before, range_length,
                                      snapshot_id):
        playlist_id = get_id('playlist', _playlist_id)
        payload = {"range_start": range_start,
                   "range_length": range_length,
                   "insert_before": insert_before}
        if snapshot_id:
            payload["snapshot_id"] = snapshot_id
        r = Route(PUT,
                  f"/users/{user}/playlists/{playlist_id}/tracks",
                  payload=payload)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def user_playlist_remove_tracks(self, user, _playlist_id, _tracks, mode, snapshot_id):
        playlist_id = get_id('playlist', _playlist_id)
        if mode == "all":
            tracks = [get_uri('track', tid) for tid in _tracks]
            payload = {"tracks": [{"uri": track} for track in tracks]}
            if snapshot_id:
                payload["snapshot_id"] = snapshot_id
        elif mode == "specific":
            tracks = []
            for tr in _tracks:
                tracks.append({
                    "uri": get_uri("track", tr["uri"]),
                    "positions": tr["positions"],
                })
            payload = {"tracks": tracks}
            if snapshot_id:
                payload["snapshot_id"] = snapshot_id
        else:
            raise LookupError("mode must be all or specific")

        r = Route(DELETE,
                  f"/users/{user}/playlists/{playlist_id}/tracks",
                  payload=payload)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def get_playlist_follower(self, playlist_owner_id, playlist_id):
        r = Route(PUT,
                  f"/users/{playlist_owner_id}/playlists/{playlist_id}/followers")

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def user_playlist_is_following(self, playlist_owner_id, playlist_id, user_ids):
        r = Route(GET,
                  "/users/{}/playlists/{}/followers/contains?ids={}"
                  .format(playlist_owner_id, playlist_id, ','.join(user_ids)))

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def featured_playlists(self, locale, country, timestamp, limit, offset):
        r = Route(GET, '/browse/featured-playlists',
                  locale=locale, country=country, timestamp=timestamp, limit=limit, offset=offset)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def new_releases(self, country, limit, offset):
        r = Route(GET,
                  '/browse/new-releases',
                  country=country, limit=limit, offset=offset)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def categories(self, country, locale, limit, offset):
        r = Route(GET,
                  '/browse/categories',
                  country=country, locale=locale, limit=limit, offset=offset)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def category_playlists(self, category_id, country, limit, offset):
        r = Route(GET,
                  '/browse/categories/' + category_id + '/playlists',
                  country=country, limit=limit, offset=offset)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def recommendations(self, seed_artists, seed_genres, seed_tracks, limit, country, **kwargs):
        params = dict(limit=limit)
        if seed_artists:
            params['seed_artists'] = ','.join(
                [get_id('artist', a) for a in seed_artists])
        if seed_genres:
            params['seed_genres'] = ','.join(seed_genres)
        if seed_tracks:
            params['seed_tracks'] = ','.join(
                [get_id('track', t) for t in seed_tracks])
        if country:
            params['market'] = country

        for attribute in ["acousticness", "danceability", "duration_ms",
                          "energy", "instrumentalness", "key", "liveness",
                          "loudness", "mode", "popularity", "speechiness",
                          "tempo", "time_signature", "valence"]:
            for prefix in ["min_", "max_", "target_"]:
                param = prefix + attribute
                if param in kwargs:
                    params[param] = kwargs[param]
        r = Route(GET, '/recommendations', **params)
        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def recommendation_genre_seeds(self):
        r = Route(GET, '/recommendations/available-genre-seeds')

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def audio_analysis(self, track_id):
        trid = get_id('track', track_id)
        r = Route(GET, f'/audio-analysis/{trid}')
        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def audio_features(self, tracks):
        if tracks is None:
            tracks = []
        if isinstance(tracks, str):
            trackid = get_id('track', tracks)
            r = Route(GET, f'/audio-features/?ids={trackid}')

            return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)
        else:
            # the response has changed, look for the new style first, and if
            # its not there, fallback on the old style
            tlist = [get_id('track', t) for t in tracks]
            r = Route(GET,
                      '/audio-features/?ids=' + ','.join(tlist))

            return await asyncio.wait_for(self.request(r, request_field='audio_features'), self.timeout, loop=self.loop)

    async def audio_analyses(self, track_ids):
        ids = get_id('track', track_ids)
        r = Route(GET, f'/audio-analysis/{ids}')

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)
