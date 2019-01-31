from twitch import TwitchClient
from secrets import client_id, OAuth

client = TwitchClient(client_id=client_id, oauth_token=OAuth)
channel = client.channels.get_by_id(44322880)

print(channel.id)
print(channel.name)
print(channel.display_name)