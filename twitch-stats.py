from secrets import client_id, OAuth
from twitch_api_service import usersget, followersget

headers = {
    'Client-ID': client_id,
}

users = [
    'Sco',
    'Thijs',
    'Sjow'
]

userIDs = usersget(headers,users)
print(userIDs)

followers_count = followersget(headers, userIDs)
print(followers_count)