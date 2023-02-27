import requests

def test_signup(email: str, password: str):
    body = {
        "email": email,
        "password": password
    }
    
    print(body)
    
    response = requests.post(url="http://127.0.0.1:1234/signup", json=body)
    return response.text

# Firebase automatically validates email string format
# beware on test cases
print(test_signup("test.email@gmail.com", "test-pass"))
