import requests
import random

head = {
    'Accept' : 'text/plain',
    'Content-type' : 'application/json'
}

payload = {
  "id": 3,
  "title": "PUT Method",
  "dueDate": "2025-08-12T11:07:58.196Z",
  "completed": True
}

response = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/3", headers=head, json=payload)

print(response.status_code)
print(response.json())
data = response.json()
print(data["id"])
assert response.status_code == 200
assert data["id"] == 3