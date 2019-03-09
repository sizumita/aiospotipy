# Aiospotipy
aiospotipy is an API wrapper for Spotify written in python.

This is based on asyncio and spotipy.

# Quick Example
```python
auth = "xxxxxxxxxxxxxx"
from aiospotipy import Spotify
spotify = Spotify(auth=auth)


# Search for an artist by its name
search_results = await spotify.search_artist(q="kalafina")

```
```python
from aiospotipy import Spotify
from aiospotipy.oauth2 import SpotifyCredentials
spotify = Spotify(SpotifyCredentials("CLIENT_ID", "CLIENT_SECRET"))

# Search for an artist by its name
search_results = await spotify.search_artist(q="kalafina")
```