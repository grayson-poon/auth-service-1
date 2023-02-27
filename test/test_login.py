import requests
import json
 
def test_login(email: str, password: str):
   body = {
       "email": email,
       "password": password
   }
   response = requests.post(url="http://127.0.0.1:1234/login", json=body)
   print(response.json())
   return json.loads(response.text)["token"]

valid_token = test_login("test.email@gmail.com", "test-pass")
invalid_token = test_login("test.email@gmail.com", "incorrect-pass")

def ping(token: str):
    headers = {
        "authorization": token
    }

    response = requests.post(url="http://127.0.0.1:1234/ping", headers=headers)
    return response.text

print(ping(valid_token), "HERE")