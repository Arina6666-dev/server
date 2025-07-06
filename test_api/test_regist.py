import requests
import uuid
import random
import string

#Успешная регистрация нового пользователя
def test_regist_success():
    register_url = "http://localhost:3000/auth/register"
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    register_payload = {
        "email": unique_email,
        "password": "1234567",
        "age": random.randint(0, 99)
    }
    register_response = requests.post(register_url, json=register_payload)
    assert register_response.status_code in [200, 201]


#Повторная регистрация
def test_regist_again():
    register_url = "http://localhost:3000/auth/register"
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    register_payload = {
        "email": unique_email,
        "password": "1234567",
        "age": random.randint(0, 99)
    }
    register_response = requests.post(register_url, json=register_payload)
    register_response_again = requests.post(register_url, json=register_payload)
    assert register_response_again.status_code in [422, 400]

#Регистрация с длинным email
def test_regist_long_email():
    register_url = "http://localhost:3000/auth/register"
    unique_email = f"{uuid.uuid4().hex[:8]*50}@gmail.com"
    register_payload = {
        "email": unique_email,
        "password": "1234567",
        "age": random.randint(0, 99)
    }
    register_response = requests.post(register_url, json=register_payload)
    assert register_response.status_code == 422

#Регистрация email без домена
def test_regist_email_no_domen():
    register_url = "http://localhost:3000/auth/register"
    unique_email = f"{uuid.uuid4().hex[:8]}"
    register_payload = {
        "email": unique_email,
        "password": "1234567",
        "age": random.randint(0, 99)
    }
    register_response = requests.post(register_url, json=register_payload)
    assert register_response.status_code == 422