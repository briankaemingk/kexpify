###
### A script that creates the spotify auth cache file
###

import settings
import os
file = open(".cache-briankaemingk", "w") 
file.write('{"token_type": "Bearer", "access_token": "' + os.environ.get("ACCESS_TOKEN") + '", "expires_in": 3600, "refresh_token": "' + os.environ.get('REFRESH_TOKEN') + '", "scope": "playlist-modify-private playlist-modify-public playlist-read-collaborative", "expires_at": 1578789444}') 
file.close() 

