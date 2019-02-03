import requests
from secrets import token_IG, client_id_IG
import urllib.request

headers = {
    'access_token': token_IG,

}

def followersget(users):
    for user in users:
        response = requests.get('https://www.instagram.com/' + user + '/?__a=1', headers=headers)

        print(response)
    return

followersget(['Bloor95'])