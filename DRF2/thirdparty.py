# It is a separate third party app.
# We are showing how to get data from API in a third party app or Web app

import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name': 'Afid',
    'roll': 101,
    'city': 'Dhaka'
}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()

print(data)
