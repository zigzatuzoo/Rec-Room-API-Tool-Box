import requests
import json

''' Enter User Cookie Here '''
cookie = ''
auth_url = 'https://auth.rec.net/connect/authorize?client_id=recnet&redirect_uri=https%3A%2F%2Frec.net%2Fauthenticate%2Fsilent&response_type=id_token%20token&scope=openid%20rn.api%20rn.notify%20rn.match.read%20rn.chat%20rn.accounts%20rn.auth%20rn.link%20rn.clubs%20rn.rooms&state=3b0bbf22ce1c40e7966dc6dd0f2df854&nonce=1ec7e44b909c416bbffae6b5e00ccb38&prompt=none'
auth_header = {'Cookie': cookie}
r = requests.get(auth_url, headers=auth_header, allow_redirects=True)

'''Acquire token from url'''
url = r.url
token = url.split("access_token=")[1].split("&token_type=")[0]
    
BToken = "Bearer " + token

print("Token: "+BToken)

userHeader= {'Authorization':BToken}

getUser = requests.get('https://api.rec.net/api/relationships/v6/current/friends?take=1000000000', headers = userHeader)

print(getUser)


dumpJson = json.dumps(getUser.json())
userJson = json.loads(dumpJson)
print(userJson)

''' All account relationships will be stored in json format in the userJson var '''