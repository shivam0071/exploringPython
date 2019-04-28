import requests

token = 'TOKEN HERE'
me = 'https://graph.facebook.com/v3.2/me?access_token='+token

me1 = requests.get(me)
print(me1.text)