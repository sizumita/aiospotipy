import asyncio
from .me import Me
from ._http import HTTPClient


class Spotify(object):
    def __init__(self, auth=None, client_credentials_manager=None, **kwargs):
        self.loop = asyncio.get_event_loop()
        self.http = HTTPClient(auth, client_credentials_manager, **kwargs)
        self.me = Me(self.http)

    async def next(self, result):
        """|coro|
        returns the next result given a paged result

        Parameters:
            - result - a previously returned paged result
        """
        return self.http.next(result)

    async def previous(self, result):
        """|coro|
        returns the previous result given a paged result

        Parameters:
            - result - a previously returned paged result
        """

        return self.http.previous(result)

    async def track(self, track_id):
        """|coro|
        returns a single track given the track's ID, URI or URL

        Parameters:
            - track_id - a spotify URI, URL or ID
        """
        return self.http.track(track_id)

    async def tracks(self, tracks, market=None):
        """|coro|
        returns a list of tracks given a list of track IDs, URIs, or URLs

        Parameters:
            - tracks - a list of spotify URIs, URLs or IDs
            - market - an ISO 3166-1 alpha-2 country code.
        """
        return self.http.tracks(tracks, market)

    async def artist(self, artist_id):
        """|coro|
        returns a single artist given the artist's ID, URI or URL

        Parameters:
            - artist_id - an artist ID, URI or URL
        """
        return self.http.artist(artist_id)

    async def artists(self, artists):
        """|coro|
        returns a list of artists given the artist IDs, URIs, or URLs

        Parameters:
            - artists - a list of  artist IDs, URIs or URLs
        """
        return self.http.artists(artists)

    async def artist_albums(self, artist_id, album_type=None, country=None, limit=20,
                            offset=0):
        """|coro|
        Get Spotify catalog information about an artist's albums

        Parameters:
            - artist_id - the artist ID, URI or URL
            - album_type - 'album', 'single', 'appears_on', 'compilation'
            - country - limit the response to one particular country.
            - limit  - the number of albums to return
            - offset - the index of the first album to return
        """
        return self.http.artist_albums(artist_id, album_type, country, limit, offset)

    async def artist_top_tracks(self, artist_id, country='US'):
        """|coro|
        Get Spotify catalog information about an artist's top 10 tracks
            by country.

        Parameters:
            - artist_id - the artist ID, URI or URL
            - country - limit the response to one particular country.
        """
        return self.http.artist_top_tracks(artist_id, country)

    async def artist_related_artists(self, artist_id):
        """|coro|
        Get Spotify catalog information about artists similar to an
            identified artist. Similarity is based on analysis of the
            Spotify community's listening history.

        Parameters:
            - artist_id - the artist ID, URI or URL
        """
        return self.http.artist_related_artists(artist_id)

    async def album(self, album_id):
        """|coro|
        returns a single album given the album's ID, URIs or URL

        Parameters:
            - album_id - the album ID, URI or URL
        """
        return self.http.album(album_id)

    async def album_tracks(self, album_id, limit=50, offset=0):
        """|coro|
        Get Spotify catalog information about an album's tracks

        Parameters:
            - album_id - the album ID, URI or URL
            - limit  - the number of items to return
            - offset - the index of the first item to return
        """
        return self.http.album_tracks(album_id, limit, offset)

    async def albums(self, albums):
        """|coro|
        returns a list of albums given the album IDs, URIs, or URLs

        Parameters:
            - albums - a list of  album IDs, URIs or URLs
        """
        return self.http.albums(albums)

    async def search(self, q, limit=10, offset=0, _type='track', market=None):
        """|coro|
        searches for an item

        Parameters:
            - q - the search query
            - limit  - the number of items to return
            - offset - the index of the first item to return
            - type - the type of item to return. One of 'artist', 'album',
                     'track' or 'playlist'
            - market - An ISO 3166-1 alpha-2 country code or the string from_token.
        """
        return self.http.search(q, limit, offset, _type, market)

    async def search_artist(self, q, limit=10, offset=0, market=None):
        """|coro|
        searches for an artist

        Parameters:
            - q - the search query
            - limit  - the number of items to return
            - offset - the index of the first item to return
            - market - An ISO 3166-1 alpha-2 country code or the string from_token.
        """
        return self.http.search_artist(q, limit, offset, market)

    async def search_album(self, q, limit=10, offset=0, market=None):
        """|coro|
        searches for an album

        Parameters:
            - q - the search query
            - limit  - the number of items to return
            - offset - the index of the first item to return
            - market - An ISO 3166-1 alpha-2 country code or the string from_token.
        """
        return self.http.search_album(q, limit, offset, market)

    async def search_track(self, q, limit=10, offset=0, market=None):
        """|coro|
        searches for an track

        Parameters:
            - q - the search query
            - limit  - the number of items to return
            - offset - the index of the first item to return
            - market - An ISO 3166-1 alpha-2 country code or the string from_token.
        """
        return self.http.search_track(q, limit, offset, market)

    async def search_playlist(self, q, limit=10, offset=0, market=None):
        """|coro|
        searches for an playlist

        Parameters:
            - q - the search query
            - limit  - the number of items to return
            - offset - the index of the first item to return
            - market - An ISO 3166-1 alpha-2 country code or the string from_token.
        """
        return self.http.search_track(q, limit, offset, market)

    async def user(self, user):
        """|coro|
        Gets basic profile information about a Spotify User

        Parameters:
            - user - the id of the usr
        """
        return self.http.user(user)

    async def user_playlists(self, user, limit=50, offset=0):
        """|coro|
        Gets playlists of a user

        Parameters:
            - user - the id of the usr
            - limit  - the number of items to return
            - offset - the index of the first item to return
        """
        return self.http.user_playlists(user, limit, offset)

    async def user_playlist(self, user, playlist_id=None, fields=None):
        """|coro|
        Gets playlist of a user

        Parameters:
            - user - the id of the user
            - playlist_id - the id of the playlist
            - fields - which fields to return
        """
        return self.http.user_playlist(user, playlist_id, fields)

    async def get_playlist_tracks(self, user, playlist_id=None, fields=None,
                                  limit=100, offset=0, market=None):
        """|coro|
        Get full details of the tracks of a playlist owned by a user.

        Parameters:
            - user - the id of the user
            - playlist_id - the id of the playlist
            - fields - which fields to return
            - limit - the maximum number of tracks to return
            - offset - the index of the first track to return
            - market - an ISO 3166-1 alpha-2 country code.
        """
        return self.http.get_playlist_tracks(user, playlist_id, fields, limit, offset, market)

    async def playlist_create(self, user, name, public=True):
        """|coro|
        Creates a playlist for a user

        Parameters:
            - user - the id of the user
            - name - the name of the playlist
            - public - is the created playlist public
        """
        return self.http.playlist_create(user, name, public)

    async def playlist_change_details(self, user, playlist_id, name=None, public=None,
                                      collaborative=None):
        """|coro|
        Changes a playlist's name and/or public/private state

        Parameters:
            - user - the id of the user
            - playlist_id - the id of the playlist
            - name - optional name of the playlist
            - public - optional is the playlist public
            - collaborative - optional is the playlist collaborative
        """
        return self.http.playlist_change_details(user, playlist_id, name, public, collaborative)

    async def unfollow_playlist(self, user, playlist_id):
        """|coro|
        Unfollows (deletes) a playlist for a user

        Parameters:
            - user - the id of the user
            - name - the name of the playlist
        """
        return self.http.unfollow_playlist(user, playlist_id)

    async def playlist_add_tracks(self, user, playlist_id, tracks, position=None):
        """|coro|
        Adds tracks to a playlist

        Parameters:
            - user - the id of the user
            - playlist_id - the id of the playlist
            - tracks - a list of track URIs, URLs or IDs
            - position - the position to add the tracks
        """
        return self.http.playlist_add_tracks(user, playlist_id, tracks, position)

    async def playlist_replace_tracks(self, user, playlist_id, tracks):
        """|coro|
        Replace all tracks in a playlist

        Parameters:
            - user - the id of the user
            - playlist_id - the id of the playlist
            - tracks - the list of track ids to add to the playlist
        """
        return self.http.playlist_replace_tracks(user, playlist_id, tracks)

    async def playlist_reorder_tracks(
            self, user, playlist_id, range_start, insert_before,
            range_length=1, snapshot_id=None):
        """|coro|
        Reorder tracks in a playlist

        Parameters:
            - user - the id of the user
            - playlist_id - the id of the playlist
            - range_start - the position of the first track to be reordered
            - range_length - optional the number of tracks to be reordered (default: 1)
            - insert_before - the position where the tracks should be inserted
            - snapshot_id - optional playlist's snapshot ID
        """
        return self.http.playlist_reorder_tracks(user, playlist_id, range_start,
                                                 insert_before, range_length, snapshot_id)

    async def playlist_remove_tracks(self, user, playlist_id, tracks, mode="all", snapshot_id=None):
        """|coro|
        Removes all occurrences of the given tracks from the given playlist

        Parameters:
            - mode - the mode of remove, `all` or `specific`
            - user - the id of the user
            - playlist_id - the id of the playlist
            - tracks - if mode is `all`:
                            the list of track ids to remove to the playlist
                       elif mode is `specific`:
                            an array of objects containing Spotify URIs of the tracks
                            to remove with their current positions in the playlist.  For example:
                            [  { "uri":"4iV5W9uYEdYUVa79Axb7Rh", "positions":[2] },
                               { "uri":"1301WleyT98MSxVHPZCA6M", "positions":[7] } ]
            - snapshot_id - optional id of the playlist snapshot
        """
        return self.http.user_playlist_remove_tracks(user, playlist_id, tracks, mode, snapshot_id)

    async def get_playlist_follower(self, playlist_owner_id, playlist_id):
        """|coro|
        Add the current authenticated user as a follower of a playlist.

        Parameters:
            - playlist_owner_id - the user id of the playlist owner
            - playlist_id - the id of the playlist

        """
        return self.http.get_playlist_follower(playlist_owner_id, playlist_id)

    async def playlist_is_following(self, playlist_owner_id, playlist_id, user_ids):
        """|coro|
        Check to see if the given users are following the given playlist

        Parameters:
            - playlist_owner_id - the user id of the playlist owner
            - playlist_id - the id of the playlist
            - user_ids - the ids of the users that you want to check to see if they follow the playlist. Maximum: 5 ids.

        """
        return self.http.user_playlist_is_following(playlist_owner_id, playlist_id, user_ids)

    async def featured_playlists(self, locale=None, country=None, timestamp=None,
                                 limit=20, offset=0):
        """|coro|
        Get a list of Spotify featured playlists

        Parameters:
            - locale - The desired language, consisting of a lowercase ISO
              639 language code and an uppercase ISO 3166-1 alpha-2 country
              code, joined by an underscore.

            - country - An ISO 3166-1 alpha-2 country code.

            - timestamp - A timestamp in ISO 8601 format:
              yyyy-MM-ddTHH:mm:ss. Use this parameter to specify the user's
              local time to get results tailored for that specific date and
              time in the day

            - limit - The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50

            - offset - The index of the first item to return. Default: 0
              (the first object). Use with limit to get the next set of
              items.
        """
        return self.http.featured_playlists(locale, country, timestamp, limit, offset)

    async def new_releases(self, country=None, limit=20, offset=0):
        """|coro|
        Get a list of new album releases featured in Spotify

        Parameters:
            - country - An ISO 3166-1 alpha-2 country code.

            - limit - The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50

            - offset - The index of the first item to return. Default: 0
              (the first object). Use with limit to get the next set of
              items.
        """
        return self.http.new_releases(country, limit, offset)

    async def categories(self, country=None, locale=None, limit=20, offset=0):
        """|coro|
        Get a list of new album releases featured in Spotify

        Parameters:
            - country - An ISO 3166-1 alpha-2 country code.
            - locale - The desired language, consisting of an ISO 639
              language code and an ISO 3166-1 alpha-2 country code, joined
              by an underscore.

            - limit - The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50

            - offset - The index of the first item to return. Default: 0
              (the first object). Use with limit to get the next set of
              items.
        """
        return self.http.categories(country, locale, limit, offset)

    async def category_playlists(self, category_id=None, country=None, limit=20, offset=0):
        """|coro|
        Get a list of new album releases featured in Spotify

        Parameters:
            - category_id - The Spotify category ID for the category.

            - country - An ISO 3166-1 alpha-2 country code.

            - limit - The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50

            - offset - The index of the first item to return. Default: 0
              (the first object). Use with limit to get the next set of
              items.
        """
        return self.http.category_playlists(category_id, country, limit, offset)

    async def recommendations(self, seed_artists=None, seed_genres=None, seed_tracks=None, limit=20, country=None,
                              **kwargs):
        """|coro|
        Get a list of recommended tracks for one to five seeds.

        Parameters:
            - seed_artists - a list of artist IDs, URIs or URLs

            - seed_tracks - a list of artist IDs, URIs or URLs

            - seed_genres - a list of genre names. Available genres for
              recommendations can be found by calling recommendation_genre_seeds

            - country - An ISO 3166-1 alpha-2 country code. If provided, all
              results will be playable in this country.

            - limit - The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 100

            - min/max/target_<attribute> - For the tuneable track attributes listed
              in the documentation, these values provide filters and targeting on
              results.
        """
        return self.http.recommendations(seed_artists, seed_genres, seed_tracks, limit, country, **kwargs)

    async def recommendation_genre_seeds(self):
        """|coro|
        Get a list of genres available for the recommendations function.
        """
        return self.http.recommendation_genre_seeds()

    async def audio_analysis(self, track_id):
        """|coro|
        Get audio analysis for a track based upon its Spotify ID

        Parameters:
            - track_id - a track URI, URL or ID
        """
        return self.http.audio_analysis(track_id)

    async def audio_features(self, tracks=None):
        """|coro|
        Get audio features for one or multiple tracks based upon their Spotify IDs

        Parameters:
            - tracks - a list of track URIs, URLs or IDs, maximum: 50 ids
        """
        return self.http.audio_features(tracks)

    async def audio_analyses(self, track_ids):
        """|coro|
        Get audio analysis for a track based upon its Spotify ID

        Parameters:
            - id - a track URIs, URLs or IDs
        """
        return self.http.audio_analyses(track_ids)
