# It is a separate third party app.
# We are showing how to get data from API in a third party app or Web app

import requests
import json

URL = "http://127.0.0.1:8000/stapicrud/"

# GET means Read operation
def get_data(id=None):
    data = {}
    headers = {'content-Type' : 'application/json'}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL,headers=headers,  data=json_data)
    data = r.json()
    print(data)


get_data()  # we are not sending id
get_data(2)  # id = 2

# POST means Create operation
def post_data():
    data = {
        'name': 'Afid',
        'roll': 222,  # if roll>200 then it will give Field Level error
        'city': 'Dhaka'  # it will give Object Level Error if it is not Dhaka
    }
    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)
post_data()


# Update operation
def update_data():
    data = {
        'id': 3,  # id should be in the database
        'name': 'Mania',
        'city': 'Dubai'
    }
    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# update_data()

# Delete operation


def delete_data():
    data = {'id': 4, }  # id should be in the database.
    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)

delete_data()
