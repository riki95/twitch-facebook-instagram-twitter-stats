import requests

def followersget(users):
    for user in users:
        response = requests.get('https://www.instagram.com/' + user + '/?__a=1')
        print(response)
    return