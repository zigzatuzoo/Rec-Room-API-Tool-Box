import requests
import json

"Enter Room Name Here"
roomName = 'ZombiesInSpaceland'


roomURL = 'https://rooms.rec.net/rooms?name=' + roomName

Headers = {'Host':'rooms.rec.net',
           'Connection':'close',
           'sec-ch-ua':'";Not A Brand";v="99", "Chromium";v="88"',
           'Accept':'*/*',
           'sec-ch-ua-mobile':'?0',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
           'Origin':'https://rec.net',
           'Sec-Fetch-Site':'same-site',
           'Sec-Fetch-Mode':'cors',
           'Sec-Fetch-Dest':'empty',
           'Referer':'https://rec.net/',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'en-US,en;q=0.9'}

roomReq = requests.get(roomURL, headers = Headers)
a = json.dumps(roomReq.json())
b = json.loads(a)

stats = b['Stats']

roomCheers = stats['CheerCount']
roomFavorites = stats['FavoriteCount']
roomVisits = stats['VisitCount']
roomVisitors = stats['VisitorCount']

print('Room Cheers: ' + str(roomCheers))
print('Room Favorites: ' + str(roomFavorites))
print('Room Visits: ' + str(roomVisits))
print('Room Visitors: ' + str(roomVisitors))

''' If you want to reference any of your room stats in a program, just add the script, remove the print values, and reference each value with the variable '''