###
### A script that creates the spotify auth cache file
###

import settings
import os
file = open(".cache-briankaemingk", "w") 
file.write('{"token_type": "Bearer", "access_token": "' + os.environ.get("ACCESS_TOKEN") + '", "expires_in": 3600, "refresh_token": "' + os.environ.get('REFRESH_TOKEN') + '", "scope": "playlist-modify-private playlist-modify-public playlist-read-collaborative", "expires_at": 1578789444}') 
file.close() 

string1 = '#encoding: utf-8'
string2 = 'SPOTIFY_USERNAME = "' + os.environ.get("SPOTIFY_USERNAME") + '"'
string3 = 'SPOTIFY_CLIENT_SECRET = "' + os.environ.get("SPOTIFY_CLIENT_SECRET") + '"'
string4 = 'SPOTIFY_CLIENT_ID = "' + os.environ.get("SPOTIFY_CLIENT_ID") + '"'
string5 = 'SPOTIFY_SCOPE = "playlist-modify-public playlist-modify-private playlist-read-collaborative"' 
string6 = 'SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"'

file = open("local_config.py", "w") 
file.write("%s\n\n%s\n%s\n%s\n%s\n%s\n" % (string1, string2, string3, string4, string5, string6))
file.close() 



