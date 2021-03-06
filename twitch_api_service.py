import requests
import json
import time  # Used it unil I get an OAuth to avoid 429 error
from secrets import client_id_TW, OAuth_TW

headers = {
    'Client-ID': client_id_TW,
}

def usersget(users):
        print('Getting user IDs...')
        users_list = []
        users_viewcounts = []
        for user in users:
                print('\tGetting ' + user)
                time.sleep(2)
                params = {
                ('login', user)
                }
                response = requests.get('https://api.twitch.tv/helix/users', headers=headers, params=params)
                json_string = response.text  # Get the text form response
                json_data = json.loads(json_string)  # Load the JSon file
                # print(json_data)
                users_list.append(json_data["data"][0]['id'])  # Get the ID
                users_viewcounts.append(json_data["data"][0]['view_count'])
        return users_list, users_viewcounts

def followersget(userIDs):
        print('Getting user followers...')
        users_followers = []
        for userID in userIDs:
                print('\tGetting ' + userID)
                time.sleep(2)
                params = (
                ('to_id', userID),
                )
                response = requests.get('https://api.twitch.tv/helix/users/follows', headers=headers, params=params)
                json_string = response.text  # Get the text form response
                json_data = json.loads(json_string)  # Load the JSon file
                # print(json_data)
                users_followers.append(json_data["total"])  # Get the Followers
        return users_followers