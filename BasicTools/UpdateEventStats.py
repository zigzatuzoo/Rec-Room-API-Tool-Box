import requests
import recnetlogin as rnl

eventID = '' 'insert the event ID here'
USER = ''
PASS = ''

token = rnl.login_to_recnet(USER, PASS).access_token
header = {'Authorization':token}

'''THE FOLLOWING VALUES ARE WHAT WILL BE UPDATED, IF NOTHING IS PROVIDED THEN IT WILL NOT BE UPDATED'''
'insert the name of the event'
eventName = ''
'insert the room name here'
roomName = ''
'insert the events description here'
eventDescription = ''
'insert privacy setting here 1 (public) or 2 (private)' 
eventPrivacy = ''
'insert image name/id here'
eventImage = '' 

roomURL = 'https://rooms.rec.net/rooms?name=' + roomName
roomReq = requests.get(roomURL)
roomID = roomReq.json()['RoomId']

eventDetails = {'RoomID':roomID,
                'Description':eventDescription,
                'Accessibility':eventPrivacy,
                'imageName':eventImage}



formatedData = ''

for value in eventDetails:
    if bool(value != '') & bool(formatedData == ''):
        formatedData = value + '=' + str(eventDetails[value])
    elif value != '':
        formatedData = formatedData +'&'+value+'='+str(eventDetails[value])
    
print(formatedData)

eventURL = 'https://api.rec.net/api/playerevents/v2/'+eventID
requests.put(eventURL, headers=header, data=formatedData)
print('Success!\n Exiting.')