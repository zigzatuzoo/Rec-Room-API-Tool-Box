from flask import Flask, render_template # pip install Flask
import requests # pip install requests
import json

'''
AUTHOR NOTE:

It may take a minute or two to load all of the images, so don't be so surprised when the program slows a bit.

Also

This is a example I made where I use the Clubs and Accounts APIs to get Top Creators' Profile pictures, and display it on a Flask web server.

This was made for the Rec Net API Toolbox created by Zigzatuzoo and Jegrade, all credits go to them for the Toolbox

Have questions or suggestions? Contact me on my active platforms:

Discord: Pythonmatics#2303
Twitter: MaticsPython
'''

class GetTopCreatorData(): # This will basically get the JSON data in the Clubs API page for Top Creators and their Account Ids
  def __init__(self):
    self.url = "https://clubs.rec.net/subscription/top/creators" # Clubs API Url
    self.page = requests.get(self.url).text # Page variable
  def __str__(self):  
    return self.page # Returns the data

def GetTopCreatorIDs(): # This will get the Creators' author IDs
  get = GetTopCreatorData() # Get the raw string data from the website...
  data = json.loads(get.page) # Then turn it into a dict...

  a = [dict(data[num]) for num, x in enumerate(data)] # Turn each piece of data into a dict...
  return a # RETURN THE BLOODY LIST

ClubIDs = [club.get("clubId") for club in GetTopCreatorIDs()] # ClubIDs
AccountIDs = [account.get("accountId") for account in GetTopCreatorIDs()] # AccountIDs
SubscriberCount = [sub.get("subscriberCount") for sub in GetTopCreatorIDs()] # SubscriberCounts


AccountURLs = [requests.get(f"https://accounts.rec.net/account/{url}").text for url in AccountIDs] # Account URLs (for each Account ID)

def GetImage(): # Get the .jpg file name from the accounts
  data = AccountURLs # shorten variable for AccountURLs
  important = 'Account' # important key name
  
  a = [{important: data[num]} for num, x in enumerate(data)] # Create a new account key called "Account"
  return a # Return the results

new_imgs = [] # Create a new images list
for img in GetImage(): # for each dict in GetImage...
  x = img.get('Account') # Extract the Account data using string slices and the find() function

  a = x.find('"profileImage":"') + len('"profileImage":"')
  b = x.find('","isJunior"')
  x = x[a:b]
  x = x.split('","bannerImage":"')
  new_imgs.append(f"<img src='https://img.rec.net/{x[0]}' width=150 height=150>") # Add the new extracted image data and turn it into a <img> tag

app = Flask(__name__) # Start a new Flask object

@app.route('/') # default App route
def index(): # function for the route
  return render_template('page.html', images=new_imgs) # Render the html file for the new_imgs list

if __name__ == '__main__': # Run the script using this (or via shell)
  app.run('0.0.0.0') # Run
