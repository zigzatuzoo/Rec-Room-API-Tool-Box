import requests
import recnetlogin as rnl
import urllib

bio = '''exampleBio'''
USER = ''
PASS = ''

parsedbio = urllib.parse.quote(bio)
print(parsedbio)

token = rnl.login_to_recnet(USER, PASS).access_token
header = {'Authorization':token}

bioUrl = 'https://accounts.rec.net/account/me/bio'

requests.put(bioUrl, headers=header, data=parsedbio)
print('Bio successfully changed, set to\n'+'URLEncode:'+parsedbio+'\nNon URLEncode:\n'+bio)
print('Done, exiting.')