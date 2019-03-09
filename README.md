# Aiospotipy
aiospotipy is an API wrapper for Spotify written in python.

This is based on asyncio and spotipy.


# Installing
This package can be installed in `pip`:
```commandline
pip install aiospotipy
```
Of course, you can install the package manually after cloning the repository:
```commandline
git clone https://github.com/sizumita/aiospotipy.git
cd aiospotipy
python setup.py install
```

# Quick Example
```python
from aiospotipy import Spotify
 
auth = "xxxxxxxxxxxxxx"
spotify = Spotify(auth=auth)
 
 
# Search for an artist by its name
search_results = await spotify.search_artist(q="kalafina")

```
```python
from aiospotipy import Spotify
from aiospotipy.oauth2 import SpotifyCredentials
 
spotify = Spotify(SpotifyCredentials("CLIENT_ID", "CLIENT_SECRET"))
 
 
# Search for an track by its id
search_results = await spotify.search(q='3n3Ppam7vgaVa1iaRUc9Lp', _type='track')
```

# License
This project is licensed under the MIT Licence.
