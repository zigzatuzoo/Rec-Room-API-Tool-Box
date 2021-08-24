import requests
import json

''' Enter User Cookie Here '''
userCookie = 'ai_user=pfp2P2zpdMxML+V0J4B+Ri|2021-08-19T17:18:45.407Z; ARRAffinity=a9d4cad7bd10f6fe1eb98ddbba36ff70b73ceb123fb4e398cf4ea51c69240ec9; ARRAffinitySameSite=a9d4cad7bd10f6fe1eb98ddbba36ff70b73ceb123fb4e398cf4ea51c69240ec9; .AspNetCore.Antiforgery.w5W7x28NAIs=CfDJ8MXx3-OwfdNOk2b7CQa2mdVK7d_8etC5yL12dMv7KY20ZvtMJd8euGRTonchFbfQpuTgayWQErhgguaZ1VgcZto3_QitHvjaFjgJNON86Q8U4GZmkB0Mtkg8RYauA9wqonDOh1Z8tyHZP8YRn1xz_xU; __stripe_mid=363ffd6c-f0c6-4022-a468-0d41896fc75868c6ba; idsrv.session=YXgNOS4zMbdomcoUyPyLPw; .AspNetCore.Identity.Application=CfDJ8MXx3-OwfdNOk2b7CQa2mdUvyzbvRlk-0NALeqg9u49qzt1uAGhnWRRDL8xoCnKEhFaIQWy_ymD23XdcZzoBGPMyz-WPnN-cESS1C8UxqUtANGZ0uTs8sfTrX5i8235LMhNasOW8jdPB0T0F1LKOXHn-6TBohT803rU9Dh-2X_S4IknCEvQv55g8w1E7linOdc13hGKJFKhllJbHAgoV6mKfcb2QlhzVfmVrKDZnbeC-Uo7zVWCHw4AhytG2_h7Q9PDYBqewh6Qn7RuMsTZLVNYwx846Q4Vg7D_MV_Vsx9aGivdb0trn-Kg_WuGIG5cgkgphjoqUqgE4T6yrPhIO3L-mEijaVtH-OEq-IJDz-YUw5oFWkFyOxdNQKhbTg9tlHE-HwdjM6cNP4vdogFJWWp9NTdfGAjMUd5QBYAosAaZMtKcEFlzKXPS4Gdsg4q6bVubv5gLnjlRw2g1K3ENuITozkDUfOrayklkSfn6GceGbsNMLQd0ziOIt15T9gNbyAjZBrJqodjC4YmGH-ydq7EtEwoLrMg7snCg1YtGt2LxK5xhsbFhsRy4doQb83Nzy79zB2ERtzUMbYR-kv7Iv-i-UA78E-0giwEgec9rPuJa1904_5XXtRhFc87LX-QmZx5xRRhpSsliMhfHP-j99FMMoLtd2jx-HlR2yR-PEva0pJnI6U8YiT8gRn2hpkZiovdNeLCmYVQ3GLQOMItmdXbw; ARRAffinity=c23827c360b38920968850b76df98b06b2f8c1f64e3d8f8f3d3a624110662108; ARRAffinitySameSite=c23827c360b38920968850b76df98b06b2f8c1f64e3d8f8f3d3a624110662108; amplitude_id_e1693a1003671058b6abc356c8ba8d59rec.net=eyJkZXZpY2VJZCI6IjIxZWE3ZjFlLTBiNTgtNDVlNC1hZWM4LTA4NWM0ZmI1ZTJhMVIiLCJ1c2VySWQiOiIxNTY4MTMiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2Mjk3MzE1NTU5NjMsImxhc3RFdmVudFRpbWUiOjE2Mjk3MzE1NTU5NjQsImV2ZW50SWQiOjYzLCJpZGVudGlmeUlkIjowLCJzZXF1ZW5jZU51bWJlciI6NjN9'

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