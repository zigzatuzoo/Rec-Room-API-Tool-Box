import requests
import json

"Enter Room Name Here"
roomName = 'ZombiesInSpaceland'


roomURL = 'https://rooms.rec.net/rooms?name=' + roomName


roomReq = requests.get(roomURL)
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