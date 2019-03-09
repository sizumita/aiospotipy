============
Aiospotipy
============

Aiospotipy is an API wrapper for Spotify written in python.

This is based on asyncio and spotipy.

Quick Example
--------------

.. code:: python

   auth = "xxxxxxxxxxxxxx"
   from aiospotipy import Spotify
   spotify = Spotify(auth=auth)


   # Search for an artist by its name
   search_results = await spotify.search_artist(q="kalafina")
