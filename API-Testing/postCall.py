import random
import requests

head = {
    "Accept" : "application/json",
    "Content-type" : "application/json",
    "Authorization": "Bearer 21fcf4c5ef4ea4490f0ad0e3256a5042953e903cfef78477ba43a0a3d37d2e3b"
}

unique_email = f"trial{random.randint(1000, 9999)}@gmail.com"

payload_request = {
    "name":"Archita Jain",
    "email":unique_email,
    "gender":"female",
    "status":"active"
}

response = requests.post("https://gorest.co.in//public/v2/users", headers=head, json=payload_request)

print(response.status_code)
print(response.json())
data = response.json()
print = data['id']

assert response.status_code == 201
# assert data['id'] == 155


