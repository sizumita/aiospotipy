import asyncio

from ._http import HTTPClient


class Spotify(object):
    def __init__(self, auth=None, client_credentials_manager=None, **kwargs):
        self.loop = asyncio.get_event_loop()
        self.http = HTTPClient(auth, client_credentials_manager, **kwargs)

    def next(self, result):
        """|coro|
        returns the next result given a paged result

        Parameters:
            - result - a previously returned paged result
        """
        return self.http.next(result)

    def previous(self, result):
        """|coro|
        returns the previous result given a paged result

        Parameters:
            - result - a previously returned paged result
        """

        return self.http.previous(result)

    def track(self, track_id):
        """|coro|
        returns a single track given the track's ID, URI or URL

        Parameters:
            - track_id - a spotify URI, URL or ID
        """
        return self.http.track(track_id)

    def tracks(self, tracks, market=None):
        """|coro|
        returns a list of tracks given a list of track IDs, URIs, or URLs

        Parameters:
            - tracks - a list of spotify URIs, URLs or IDs
            - market - an ISO 3166-1 alpha-2 country code.
        """
        return self.http.tracks(tracks, market)

    def artist(self, artist_id):
        """|coro|
        returns a single artist given the artist's ID, URI or URL

        Parameters:
            - artist_id - an artist ID, URI or URL
        """
        return self.http.artist(artist_id)

    def artists(self, artists):
        """|coro|
        returns a list of artists given the artist IDs, URIs, or URLs

        Parameters:
            - artists - a list of  artist IDs, URIs or URLs
        """
        return self.http.artists(artists)

    def artist_albums(self, artist_id, album_type=None, country=None, limit=20,
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

    def artist_top_tracks(self, artist_id, country='US'):
        """|coro|
        Get Spotify catalog information about an artist's top 10 tracks
            by country.

        Parameters:
            - artist_id - the artist ID, URI or URL
            - country - limit the response to one particular country.
        """
        return self.http.artist_top_tracks(artist_id, country)

    def artist_related_artists(self, artist_id):
        """|coro|
        Get Spotify catalog information about artists similar to an
            identified artist. Similarity is based on analysis of the
            Spotify community's listening history.

        Parameters:
            - artist_id - the artist ID, URI or URL
        """
        return self.http.artist_related_artists(artist_id)

    def album(self, album_id):
        """|coro|
        returns a single album given the album's ID, URIs or URL

        Parameters:
            - album_id - the album ID, URI or URL
        """
        return self.http.album(album_id)

    def album_tracks(self, album_id, limit=50, offset=0):
        """|coro|
        Get Spotify catalog information about an album's tracks

        Parameters:
            - album_id - the album ID, URI or URL
            - limit  - the number of items to return
            - offset - the index of the first item to return
        """
        return self.http.album_tracks(album_id, limit, offset)

    def albums(self, albums):
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

    def search_artist(self, q, limit=10, offset=0, market=None):
        """|coro|
        searches for an artist

        Parameters:
            - q - the search query
            - limit  - the number of items to return
            - offset - the index of the first item to return
            - market - An ISO 3166-1 alpha-2 country code or the string from_token.
        """
        return self.http.search_artist(q, limit, offset, market)

    def search_album(self, q, limit=10, offset=0, market=None):
        """|coro|
        searches for an album

        Parameters:
            - q - the search query
            - limit  - the number of items to return
            - offset - the index of the first item to return
            - market - An ISO 3166-1 alpha-2 country code or the string from_token.
        """
        return self.http.search_album(q, limit, offset, market)

    def search_track(self, q, limit=10, offset=0, market=None):
        """|coro|
        searches for an track

        Parameters:
            - q - the search query
            - limit  - the number of items to return
            - offset - the index of the first item to return
            - market - An ISO 3166-1 alpha-2 country code or the string from_token.
        """
        return self.http.search_track(q, limit, offset, market)

    def search_playlist(self, q, limit=10, offset=0, market=None):
        """|coro|
        searches for an playlist

        Parameters:
            - q - the search query
            - limit  - the number of items to return
            - offset - the index of the first item to return
            - market - An ISO 3166-1 alpha-2 country code or the string from_token.
        """
        return self.http.search_track(q, limit, offset, market)

    def user(self, user):
        """|coro|
        Gets basic profile information about a Spotify User

        Parameters:
            - user - the id of the usr
        """
        return self.http.user(user)

    def current_user_playlists(self, limit=50, offset=0):
        """|coro|
        Get current user playlists without required getting his profile

        Parameters:
            - limit  - the number of items to return
            - offset - the index of the first item to return
        """
        return self.http.current_user_playlists(limit, offset)

    def user_playlists(self, user, limit=50, offset=0):
        """|coro|
        Gets playlists of a user

        Parameters:
            - user - the id of the usr
            - limit  - the number of items to return
            - offset - the index of the first item to return
        """
        return self.http.user_playlists(user, limit, offset)

    def user_playlist(self, user, playlist_id=None, fields=None):
        """|coro|
        Gets playlist of a user

        Parameters:
            - user - the id of the user
            - playlist_id - the id of the playlist
            - fields - which fields to return
        """
        return self.http.user_playlist(user, playlist_id, fields)

    def user_playlist_tracks(self, user, playlist_id=None, fields=None,
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
        return self.http.user_playlist_tracks(user, playlist_id, fields, limit, offset, market)

    def user_playlist_create(self, user, name, public=True):
        """|coro|
        Creates a playlist for a user

        Parameters:
            - user - the id of the user
            - name - the name of the playlist
            - public - is the created playlist public
        """
        return self.http.user_playlist_create(user, name, public)

    def user_playlist_change_details(self, user, playlist_id, name=None, public=None,
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
        return self.http.user_playlist_change_details(user, playlist_id, name, public, collaborative)

    def user_playlist_unfollow(self, user, playlist_id):
        """|coro|
        Unfollows (deletes) a playlist for a user

        Parameters:
            - user - the id of the user
            - name - the name of the playlist
        """
        return self.http.user_playlist_unfollow(user, playlist_id)

    def user_playlist_add_tracks(self, user, playlist_id, tracks, position=None):
        """|coro|
        Adds tracks to a playlist

        Parameters:
            - user - the id of the user
            - playlist_id - the id of the playlist
            - tracks - a list of track URIs, URLs or IDs
            - position - the position to add the tracks
        """
        return self.http.user_playlist_add_tracks(user, playlist_id, tracks, position)

    def user_playlist_replace_tracks(self, user, playlist_id, tracks):
        """|coro|
        Replace all tracks in a playlist

        Parameters:
            - user - the id of the user
            - playlist_id - the id of the playlist
            - tracks - the list of track ids to add to the playlist
        """
        return self.http.user_playlist_replace_tracks(user, playlist_id, tracks)

    def user_playlist_reorder_tracks(
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
        return self.http.user_playlist_reorder_tracks(user, playlist_id, range_start,
                                                      insert_before, range_length, snapshot_id)

    def user_playlist_remove_all_occurrences_of_tracks(
            self, user, playlist_id, tracks, snapshot_id=None):
        """|coro|
        Removes all occurrences of the given tracks from the given playlist

        Parameters:
            - user - the id of the user
            - playlist_id - the id of the playlist
            - tracks - the list of track ids to add to the playlist
            - snapshot_id - optional id of the playlist snapshot

        """
        return self.http.user_playlist_remove_all_occurrences_of_tracks(user, playlist_id, tracks, snapshot_id)

    def user_playlist_remove_specific_occurrences_of_tracks(
            self, user, playlist_id, tracks, snapshot_id=None):
        """|coro|
        Removes all occurrences of the given tracks from the given playlist

        Parameters:
            - user - the id of the user
            - playlist_id - the id of the playlist
            - tracks - an array of objects containing Spotify URIs of the tracks to remove with their current positions in the playlist.  For example:
                [  { "uri":"4iV5W9uYEdYUVa79Axb7Rh", "positions":[2] },
                   { "uri":"1301WleyT98MSxVHPZCA6M", "positions":[7] } ]
            - snapshot_id - optional id of the playlist snapshot
        """
        return self.http.user_playlist_remove_specific_occurrences_of_tracks(user, playlist_id, tracks, snapshot_id)

    def user_playlist_follow_playlist(self, playlist_owner_id, playlist_id):
        """|coro|
        Add the current authenticated user as a follower of a playlist.

        Parameters:
            - playlist_owner_id - the user id of the playlist owner
            - playlist_id - the id of the playlist

        """
        return self.http.user_playlist_follow_playlist(playlist_owner_id, playlist_id)

    def user_playlist_is_following(self, playlist_owner_id, playlist_id, user_ids):
        """|coro|
        Check to see if the given users are following the given playlist

        Parameters:
            - playlist_owner_id - the user id of the playlist owner
            - playlist_id - the id of the playlist
            - user_ids - the ids of the users that you want to check to see if they follow the playlist. Maximum: 5 ids.

        """
        return self.http.user_playlist_is_following(playlist_owner_id, playlist_id, user_ids)

    def me(self):
        """|coro|
        Get detailed profile information about the current user.
            An alias for the 'current_user' method.
        """
        return self.http.me()

    def current_user(self):
        """|coro|
        Get detailed profile information about the current user.
            An alias for the 'me' method.
        """
        return self.http.current_user()

    def current_user_saved_albums(self, limit=20, offset=0):
        """|coro|
        Gets a list of the albums saved in the current authorized user's
            "Your Music" library

        Parameters:
            - limit - the number of albums to returnx
            - offset - the index of the first album to return

        """
        return self.http.current_user_saved_albums(limit, offset)

    def current_user_saved_tracks(self, limit=20, offset=0):
        """|coro|
        Gets a list of the tracks saved in the current authorized user's
            "Your Music" library

        Parameters:
            - limit - the number of tracks to return
            - offset - the index of the first track to return

        """
        return self.http.current_user_saved_tracks(limit, offset)

    def current_user_followed_artists(self, limit=20, after=None):
        """|coro|
        Gets a list of the artists followed by the current authorized user

        Parameters:
            - limit - the number of tracks to return
            - after - ghe last artist ID retrieved from the previous request

        """
        return self.http.current_user_followed_artists(limit, after)

    def current_user_saved_tracks_delete(self, tracks=None):
        """|coro|
        Remove one or more tracks from the current user's
            "Your Music" library.

        Parameters:
            - tracks - a list of track URIs, URLs or IDs
        """
        return self.http.current_user_saved_tracks_delete(tracks)

    def current_user_saved_tracks_contains(self, tracks=None):
        """|coro|
        Check if one or more tracks is already saved in
            the current Spotify user’s “Your Music” library.

        Parameters:
            - tracks - a list of track URIs, URLs or IDs
        """
        return self.http.current_user_saved_tracks_contains(tracks)

    def current_user_saved_tracks_add(self, tracks=None):
        """|coro|
        Add one or more tracks to the current user's
            "Your Music" library.

        Parameters:
            - tracks - a list of track URIs, URLs or IDs
        """
        return self.http.current_user_saved_tracks_add(tracks)

    def current_user_top_artists(self, limit=20, offset=0, time_range='medium_term'):
        """|coro|
        Get the current user's top artists

        Parameters:
            - limit - the number of entities to return
            - offset - the index of the first entity to return
            - time_range - Over what time frame are the affinities computed
              Valid-values: short_term, medium_term, long_term
        """
        return self.http.current_user_top_artists(limit, offset, time_range)

    def current_user_top_tracks(self, limit=20, offset=0, time_range='medium_term'):
        """|coro|
        Get the current user's top tracks

        Parameters:
            - limit - the number of entities to return
            - offset - the index of the first entity to return
            - time_range - Over what time frame are the affinities computed
              Valid-values: short_term, medium_term, long_term
        """
        return self.http.current_user_top_tracks(limit, offset, time_range)

    def current_user_saved_albums_add(self, albums=None):
        """|coro|
        Add one or more albums to the current user's
            "Your Music" library.

        Parameters:
            - albums - a list of album URIs, URLs or IDs
        """
        return self.http.current_user_saved_albums_add(albums)

    def featured_playlists(self, locale=None, country=None, timestamp=None,
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

    def new_releases(self, country=None, limit=20, offset=0):
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

    def categories(self, country=None, locale=None, limit=20, offset=0):
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

    def category_playlists(self, category_id=None, country=None, limit=20, offset=0):
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

    def recommendations(self, seed_artists=None, seed_genres=None, seed_tracks=None, limit=20, country=None, **kwargs):
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

    def recommendation_genre_seeds(self):
        """|coro|
        Get a list of genres available for the recommendations function.
        """
        return self.http.recommendation_genre_seeds()

    def audio_analysis(self, track_id):
        """|coro|
        Get audio analysis for a track based upon its Spotify ID

        Parameters:
            - track_id - a track URI, URL or ID
        """
        return self.http.audio_analysis(track_id)

    def audio_features(self, tracks=None):
        """|coro|
        Get audio features for one or multiple tracks based upon their Spotify IDs

        Parameters:
            - tracks - a list of track URIs, URLs or IDs, maximum: 50 ids
        """
        return self.http.audio_features(tracks)

    def audio_analyses(self, track_ids):
        """|coro|
        Get audio analysis for a track based upon its Spotify ID

        Parameters:
            - id - a track URIs, URLs or IDs
        """
        return self.http.audio_analyses(track_ids)
