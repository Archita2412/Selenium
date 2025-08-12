# import requests
# import random

# head = {
#     "Accept" : "application/json",
#     "Content-type" : "application/json",
#     "Authorization" : "Bearer 21fcf4c5ef4ea4490f0ad0e3256a5042953e903cfef78477ba43a0a3d37d2e3b"
# }

# unique_email = f"trial{random.randint(1000,9999)}@gmail.com"

# payload = {
#     "post_id": 162504,
#     # "post_id":230560,
#     "name": "Mr. Chatura Mukhopadhyay",
#     "email": "chatura_mr_mukhopadhyay@mertz.test",
#     "body": "Velit sequi nihil. Libero reprehenderit molestiae."
# }

# comment_id = 162494
# response = requests.put(f"https://gorest.co.in/public/v2/users/{comment_id}", headers=head)

# print(response.status_code)
# print(response.json())

import requests
import random

head = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer 21fcf4c5ef4ea4490f0ad0e3256a5042953e903cfef78477ba43a0a3d37d2e3b"
}

payload = {
    "post_id": 162504,
    "name": "Mr. Chatura Mukhopadhyay",
    "email": "chatura_mr_mukhopadhyay@mertz.test",
    "body": "Velit sequi nihil. Libero reprehenderit molestiae."
}

comment_id = 162494  # This must be a real comment ID that exists
response = requests.put(
    f"https://gorest.co.in/public/v2/comments/{comment_id}",
    headers=head,
    json=payload
)

print(response.status_code)
print(response.json())
