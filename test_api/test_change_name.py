import requests
import uuid
import random
import string

def test_change_user_name_success():
    register_url = "http://localhost:3000/auth/register"
    unique_email = f"user_{uuid.uuid4().hex[:8]}@gmail.com"
    register_payload = {
        "email": unique_email,
        "password": "1234567",
        "age": random.randint(0, 99)
    }
    register_response = requests.post(register_url, json=register_payload)
    assert register_response.status_code in [200, 201]

    login_url = "http://localhost:3000/auth/login"
    login_response = requests.post(login_url, json={
        "email": unique_email,
        "password": "1234567"
    })
    assert login_response.status_code == 200

    token = login_response.json().get("token")

    name_url = "http://localhost:3000/user/name"
    new_name = {"name": "paupau"}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.patch(name_url, json=new_name, headers=headers)
    
    assert response.status_code == 200