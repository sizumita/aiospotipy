from ._http import (HTTPClient,
                    get_id,
                    Route,
                    GET,
                    PUT,
                    DELETE,
                    )
import asyncio


class Me:
    def __init__(self, _http: HTTPClient):
        self.http = _http
        self.request = _http.request
        self.timeout = _http.timeout
        self.loop = _http.loop

    async def user(self):
        """|coro|
        Get detailed profile information about the current user.
            An alias for the 'current_user' method.
        """
        r = Route(GET, '/me/')
        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def playlists(self, limit=50, offset=0):
        """|coro|
        Get current user playlists without required getting his profile

        Parameters:
            - limit  - the number of items to return
            - offset - the index of the first item to return
        """
        r = Route(GET, "/me/playlists", limit=limit, offset=offset)
        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def albums(self, limit=20, offset=0):
        """|coro|
        Gets a list of the albums saved in the current authorized user's
            "Your Music" library

        Parameters:
            - limit - the number of albums to returnx
            - offset - the index of the first album to return

        """
        r = Route(GET,
                  '/me/albums',
                  limit=limit, offset=offset)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def tracks(self, limit=20, offset=0):
        """|coro|
        Gets a list of the tracks saved in the current authorized user's
            "Your Music" library

        Parameters:
            - limit - the number of tracks to return
            - offset - the index of the first track to return

        """
        r = Route(GET,
                  '/me/tracks',
                  limit=limit, offset=offset)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def followed_artists(self, limit=20, after=None):
        """|coro|
        Gets a list of the artists followed by the current authorized user

        Parameters:
            - limit - the number of tracks to return
            - after - ghe last artist ID retrieved from the previous request
        """
        r = Route(GET,
                  '/me/following',
                  type='artist', limit=limit, after=after)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def delete_tracks(self, tracks=None):
        """|coro|
        Remove one or more tracks from the current user's
            "Your Music" library.

        Parameters:
            - tracks - a list of track URIs, URLs or IDs
        """
        track_list = []
        if tracks:
            track_list = [get_id('track', t) for t in tracks]
        r = Route(DELETE,
                  '/me/tracks/?ids=' + ','.join(track_list))

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def contains_tracks(self, tracks=None):
        """|coro|
        Check if one or more tracks is already saved in
            the current Spotify user’s “Your Music” library.

        Parameters:
            - tracks - a list of track URIs, URLs or IDs
        """
        track_list = []
        if tracks is not None:
            track_list = [get_id('track', t) for t in tracks]
        r = Route(GET,
                  '/me/tracks/contains?ids=' + ','.join(track_list))

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def add_tracks(self, tracks=None):
        """|coro|
        Add one or more tracks to the current user's
            "Your Music" library.

        Parameters:
            - tracks - a list of track URIs, URLs or IDs
        """
        track_list = []
        if tracks is not None:
            track_list = [get_id('track', t) for t in tracks]
        r = Route(PUT,
                  '/me/tracks/?ids=' + ','.join(track_list))

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def top_artists(self, limit=20, offset=0, time_range='medium_term'):
        """|coro|
        Get the current user's top artists

        Parameters:
            - limit - the number of entities to return
            - offset - the index of the first entity to return
            - time_range - Over what time frame are the affinities computed
              Valid-values: short_term, medium_term, long_term
        """
        r = Route(GET,
                  '/me/top/artists',
                  time_range=time_range, limit=limit, offset=offset)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def my_top_tracks(self, limit=20, offset=0, time_range='medium_term'):
        """|coro|
        Get the current user's top tracks

        Parameters:
            - limit - the number of entities to return
            - offset - the index of the first entity to return
            - time_range - Over what time frame are the affinities computed
              Valid-values: short_term, medium_term, long_term
        """
        r = Route(GET,
                  '/me/top/tracks',
                  time_range=time_range, limit=limit, offset=offset)

        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)

    async def add_albums(self, albums=None):
        """|coro|
        Add one or more albums to the current user's
            "Your Music" library.

        Parameters:
            - albums - a list of album URIs, URLs or IDs
        """
        if albums is None:
            albums = []
        alist = [get_id('album', a) for a in albums]
        r = Route(PUT,
                  '/me/albums?ids=' + ','.join(alist))
        return await asyncio.wait_for(self.request(r), self.timeout, loop=self.loop)