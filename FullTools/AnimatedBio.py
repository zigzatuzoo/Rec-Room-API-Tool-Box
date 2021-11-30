import requests
import recnetlogin as rnl
import urllib
import time

bio1 = '''Loading.'''
bio2 = '''Loading..'''
bio3 = '''Loading...'''
pauseTime = 1

USER = ''
PASS = ''

token = rnl.login_to_recnet(USER, PASS).access_token
header = {'Authorization':token}

bioUrl = 'https://accounts.rec.net/account/me/bio'



def updateBio(bio):
    parsedbio = urllib.parse.quote(bio)
    print('changing bio to: \n' +parsedbio)
    requests.put(bioUrl, headers=header, data=parsedbio)
    time.sleep(pauseTime)
    
while 1==1:
    updateBio(bio1)
    updateBio(bio2)
    updateBio(bio3)
    updateBio(bio2)