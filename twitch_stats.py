from twitch_api_service import usersget, followersget


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

def twitch_get():
    user_IDs, user_viewcounts = usersget(users)
    followers_count = followersget(user_IDs)

    return users, user_IDs, user_viewcounts, followers_count