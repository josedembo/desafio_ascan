import requests
from faker import Faker
import json
import os
import sys
import csv

directory = "data_users"

if not os.path.exists(directory):
    os.makedirs(directory)

base_url_1 = "http://localhost:5000/api/v1/auth/login"
base_url_2 = "http://localhost:5000/api/v1/subscriptions"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

number_of_subscriptions = int(sys.argv[1])

fk = Faker()

users_data = []

with open(f"{directory}/users.csv", "r") as users_file:
    reader = csv.reader(users_file)
    data = list(reader)
    for index, user in enumerate(data):
        if index > number_of_subscriptions:
            break
        
        if index == 0:
            continue
    
        email = user[2]
        password  = user[1]
        
        data = json.dumps({
            "email": email,
            "password": password
        })
        
        response = requests.post(url=base_url_1, headers=headers, data=data)
        # print(response.json())
        
        token = response.json()["token"]
        
        headers_2 = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
        }
        
        response_2 = requests.post(url=base_url_2, headers=headers_2)
        
        
        
        
        