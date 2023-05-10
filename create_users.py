import requests
from faker import Faker
import json
import os
import sys
import csv

directory = "data_users"

if not os.path.exists(directory):
    os.makedirs(directory)

base_url = "http://localhost:5000/api/v1/auth/register"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

number_of_users = int(sys.argv[1])

fk = Faker()

users_data = []
header = ["username", "password", "email", "full_name"]

for index in range(number_of_users):
  
    first_name = fk.unique.first_name()
    last_name = fk.unique.last_name()
    username = f"{first_name}{index}"
    password = fk.password()
    email = f"{first_name}.{last_name}{index}@{fk.unique.domain_name()}"
    full_name = f"{first_name} {last_name}"

    data = {
        "username": username,
        "password": password,
        "email": email,
        "full_name": full_name
    }

    json_data = json.dumps(data)

    users = requests.post(url=base_url, headers=headers, data=json_data)
    
    users_data.append(data)

    print(data)
    print(users)

with open(f"{directory}/users.csv", "w") as users_file:
    file = csv.writer(users_file)
    file.writerow(header)
    for user in users_data:
        file.writerow(user.values())
        