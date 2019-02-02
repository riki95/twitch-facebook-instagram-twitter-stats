from secrets import client_id, OAuth
from twitch_api_service import usersget, followersget
import csv

headers = {
    'Client-ID': client_id,
}

users = [
    'Cicciogamer89',
    'TonyTubo',
    'LosAmigos',
    'PiazzTwitch',
    'IlGattoSulTubo',
    'MarcusKron',
    'CKibe',
    'iTermosifoni',
    'VKingplays',
    'Budilicious',
    'Urcailduca',
    'PolyHS',
    'Nerdoardo',
    'Nerdocracy',
    'Berrofronzo',
    'Bloor95',
    'Gera89',
    'Shiftymine',
    'Turbo_feto',
    'Illness95',
    'Bunnyhoppor',
    'Kikko',
    'NishaStreaming',
]

userIDs = usersget(headers,users)

followers_count = followersget(headers, userIDs)

with open('twitch.csv', mode='w') as twitchcsv:
    print('Creating CSV...')
    twitch_writer = csv.writer(twitchcsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    twitch_writer.writerow(['Username', 'UserID', 'Link', 'Followers'])  # Create first Row
    for i in range(len(users)):
        twitch_writer.writerow([users[i], userIDs[i], 'twitch.tv/' + users[i], followers_count[i]])

print('Done!')