from secrets import client_id, OAuth
from twitch_api_service import usersget, followersget
import csv

headers = {
    'Client-ID': client_id,
}

users = [
    'Sco',
    'Thijs',
    'Sjow'
]

userIDs = usersget(headers,users)

followers_count = followersget(headers, userIDs)

with open('twitch.csv', mode='w') as twitchcsv:
    twitch_writer = csv.writer(twitchcsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    twitch_writer.writerow(['Username', 'UserID', 'Followers'])
    for i in range(len(users)):
        twitch_writer.writerow([users[i], userIDs[i], followers_count[i]])