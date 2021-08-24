import requests
import json

''' Enter User Cookie Here '''
userCookie = ''

authHeader= {'Host' : 'auth.rec.net',
             'Connection' : 'close',
             'sec-ch-ua' : '";Not A Brand";v="99", "Chromium",v="88"',
             'sec-ch-ua-mobile' : '?0',
             'Upgrade-Insecure-Requests' : '1',
             'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
             'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
             'Sec-Fetch-Site' : 'same-site',
             'Sec-Fetch-Mode' : 'navigate',
             'Sec-Fetch-Dest' : 'iframe',
             'Referer' : 'https://rec.net',
             'Accept-Encoding' : 'gzip, deflate',
             'Accept-Language' : 'en-US,en;q=0.9',
             'Cookie' : userCookie
             }

''' Actual Auth Request '''
authR = requests.get('https://auth.rec.net/connect/authorize?client_id=recnet&redirect_uri=https%3A%2F%2Frec.net%2Fauthenticate%2Fsilent&response_type=id_token%20token&scope=openid%20rn.api%20rn.notify%20rn.match.read%20rn.chat%20rn.accounts%20rn.auth%20rn.link%20rn.clubs%20rn.rooms&state=db44e0c9666b477d8415b8a3366a390e&nonce=e2d5f234c23d4c05bf2b5ecdfbd4e536&prompt=none&id_token_hint=eyJhbGciOiJSUzI1NiIsImtpZCI6IjRwY2dIaFlHWXk0LTZsUDI5d0RDME1kS09ONCIsInR5cCI6IkpXVCIsIng1dCI6IjRwY2dIaFlHWXk0LTZsUDI5d0RDME1kS09ONCJ9.eyJuYmYiOjE2Mjk0ODM1OTgsImV4cCI6MTYyOTQ4Mzg5OCwiaXNzIjoiaHR0cHM6Ly9hdXRoLnJlYy5uZXQiLCJhdWQiOiJyZWNuZXQiLCJub25jZSI6IjFhZWQwMzAyODg0OTQ1ZmFhYzk5OGUzNmZjNjhjOGZmIiwiaWF0IjoxNjI5NDgzNTk4LCJhdF9oYXNoIjoidnNnbEtCME5TNkU1UUV2Y2JJWk1rdyIsInNfaGFzaCI6ImJ2M3FTV2szbXAzWW5jTEFtajd5c3ciLCJzaWQiOiJZWGdOT1M0ek1iZG9tY29VeVB5TFB3Iiwic3ViIjoiMTU2ODEzIiwiYXV0aF90aW1lIjoxNjI5NDgzNTk1LCJpZHAiOiJsb2NhbCIsImFtciI6WyJwd2QiXX0.M8mMN2oflb2rDotYOVPF75TAU8dGno2iQS0njYUX2TH23L9Kcm1E-ILbSiJNytX8EiMHfOvr_HRvHDGqyAXF3YeU2LkYXw_qCB89poizImxnJQP9-MyDVdolU_FId01QeEsRF2nuRz3lhYUt0RuUdnJfVM5Rt2wl7DuKKG_bsnLETmzSXswYJYNku8HHlqOLECBoFv7DMG3V1uFHLw1c4F7j42OP_-6mqt2y92XRwpgHOxup5X0bSCCRCYPzJiFvaDWAzFIIeMdnUhK8EEI9471V3MVCE3ju5BJoENLGtRMC9tjy88DU7TInczrqNBTVH7xdPygLpkIPDLczM4Nqkg', headers = authHeader, allow_redirects=True)
    
nonbtoken = authR.url[942:2038]
    
BToken = "Bearer " + nonbtoken

print(BToken)

userHeader= {'Host':'api.rec.net',
             'Sec-Ch-Ua':'" Not A;Brand";v="99", "Chromium";v="92"',
             'Accept':'*/*',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
             'Sec-Ch-Ua-Mobile':'?0',
             'Authorization':BToken,
             'Origin':'https://rec.net',
             'Sec-Fetch-Site':'same-site',
             'Sec-Fetch-Mode':'cors',
             'Sec-Fetch-Dest':'empty',
             'Referer':'https://rec.net/',
             'Accept-Encoding':'gzip, deflate',
             'Accept-Language':'en-US,en;q=0.9',
             'Connection':'close',}

getUser = requests.get('https://api.rec.net/api/relationships/v6/current/friends?take=1000000000', headers = userHeader)

print(getUser)


dumpJson = json.dumps(getUser.json())
userJson = json.loads(dumpJson)
print(userJson)

''' All account relationships will be stored in json format in the userJson var '''