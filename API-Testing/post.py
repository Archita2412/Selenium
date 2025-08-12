import random
import requests

head = {
    "Accept" : "text/plain",
    "Content-type" : "application/json",
    # "Authorization": "Bearer 21fcf4c5ef4ea4490f0ad0e3256a5042953e903cfef78477ba43a0a3d37d2e3b"
}

unique_email = f"trial{random.randint(1000, 9999)}@gmail.com"

payload_request = {
  "id": 0,
  "title": "string",
  "dueDate": "2025-08-12T11:00:06.533Z",
  "completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head, json=payload_request)

print(response.status_code)
print(response.json())
data = response.json()
print = data["id"]

assert response.status_code == 200
assert data["id"] == 155


