import requests
import json
import recnetlogin as rnl

print('If you do not feel safe giving this program your password please open the code in your text editor of choice and audit the code yourself.')

user = input('Please put your RR@ here\n')
passwd = input('Please put your RR account pass here\n')
print('logging in')
token = rnl.login_to_recnet(user,passwd).access_token
tokenAuth = {}
tokenAuth["Authorization"] = token
print('logged successfully')

friendsUrl = 'https://api.rec.net/api/relationships/v6/current/friends?take=1000000000'
getUser = requests.get(friendsUrl, headers=tokenAuth)
dumpJson = json.dumps(getUser.json())
userJson = json.loads(dumpJson)

print(userJson)

for userInfo in userJson:
    if userInfo['Favorited'] == 3:

        unFaveUrl = 'https://api.rec.net/api/relationships/v1/unfavorite?id=' + str(userInfo['PlayerID'])
        requests.get(unFaveUrl,headers=tokenAuth)
        print('Unfaving ID: '+str(userInfo['PlayerID']))
print('This might not have unfavorited everyone if you have a lot of friends, in this case please run this a couple times ')