import csv
from twitch_stats import twitch_get

users, user_IDs, user_viewcounts, followers_count = twitch_get()

with open('twitch.csv', mode='w') as twitchcsv:
    print('Creating CSV...')
    twitch_writer = csv.writer(twitchcsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    twitch_writer.writerow(['Username', 'UserID', 'Link', 'Followers', 'Views'])  # Create first Row
    for i in range(len(users)):
        twitch_writer.writerow([users[i], user_IDs[i], 'twitch.tv/' + users[i], followers_count[i], user_viewcounts[i]])