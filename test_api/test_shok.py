import requests
import uuid
import random

#Пользователь в ШОКе
def test_exist_user():
    url = "http://localhost:3000/auth/register"
    unique_email = f"user_{uuid.uuid4().hex[:8]}@gmail.com"
    unique_age = random.randint(0, 99)
    payload = {
        "email": unique_email,
        "password": "1234567",
        "age": unique_age
    }
    response = requests.post(url, json=payload)

    url = "http://localhost:3000/exist"
    payload = {
        "email":  unique_email
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "exist" in data
    assert data["exist"] is True


#Пользователь не в ШОКе
def test_not_exist_user():
    url = "http://localhost:3000/exist"
    payload = {
        "email": "newuser@gmail.com"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "exist" in data
    assert data["exist"] is False