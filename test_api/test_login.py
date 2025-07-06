import requests
import uuid
import random
import string

#Успешное залогинивание
def test_login():
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


#Залогинивание с неверным пароллем
def test_login():
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
        "password": "000000000000000"
    })
    assert login_response.status_code == 422
