import requests
import json
import recnetlogin as rnl

username = 'exampleUsername'
passwd = 'examplePassword'

BToken = rnl.login_to_recnet(username,passwd).access_token
print(BToken)
userHeader= {'Authorization':BToken}

getUser = requests.get('https://api.rec.net/api/relationships/v6/current/friends?take=1000000000', headers = userHeader)

print(getUser)


dumpJson = json.dumps(getUser.json())
userJson = json.loads(dumpJson)
print(userJson)

''' All account relationships will be stored in json format in the userJson var '''