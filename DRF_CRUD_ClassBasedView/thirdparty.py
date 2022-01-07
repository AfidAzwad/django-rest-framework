# It is a separate third party app.
# We are showing how to get data from API in a third party app or Web app

import requests
import json

URL = "http://127.0.0.1:8000/studentcrud/"

# GET means Read operation
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


get_data()  # we are not sending id
get_data(2)  # id = 2

# POST means Create operation
def post_data():
    data = {
        'name': 'Sania',
        'roll': 104,
        'city': 'Dubai'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)
post_data()

# Update operation
def update_data():
    data = {
        'id': 3, # id should be in the database
        'name': 'Mania',
        'city': 'Dubai'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

update_data()

# Delete operation
def delete_data():
    data = {'id': 4,} # id should be in the database
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

delete_data()