# It is a separate third party app. 
# We are showing how to get data from API in a third party app or Web app

import requests

URL = "http://127.0.0.1:8000/stuinfo/"

r = requests.get(url = URL)

data = r.json()

print(data)