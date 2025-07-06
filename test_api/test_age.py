import requests
import uuid
import random
import string

#тестирование граничного значения 0
def test_zero_number():
    register_url = "http://localhost:3000/auth/register"
    unique_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    register_payload = {
        "email": unique_email,
        "password": "TestPassword123",
        "age": 0
    }
    register_response = requests.post(register_url, json=register_payload)
    assert register_response.status_code == 200


#тестирование граничного значения 99
def test_ninenine_number():
    register_url = "http://localhost:3000/auth/register"
    unique_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    register_payload = {
        "email": unique_email,
        "password": "TestPassword123",
        "age": 99
    }
    register_response = requests.post(register_url, json=register_payload)
    assert register_response.status_code == 200   

#тестирование граничного значения >99
def test_toobig_number():
    register_url = "http://localhost:3000/auth/register"
    unique_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    register_payload = {
        "email": unique_email,
        "password": "TestPassword123",
        "age": random.randint(100, 200)
    }
    register_response = requests.post(register_url, json=register_payload)
    assert register_response.status_code == 422

#тестирование отрицательного возраста
def test_negative_number():
    register_url = "http://localhost:3000/auth/register"
    unique_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    register_payload = {
        "email": unique_email,
        "password": "TestPassword123",
        "age": random.randint(-10, -1)
    }
    register_response = requests.post(register_url, json=register_payload)
    assert register_response.status_code == 422

#тестирование пустого возраста
def test_null_number():
    register_url = "http://localhost:3000/auth/register"
    unique_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    register_payload = {
        "email": unique_email,
        "password": "TestPassword123",
        "age": ''
    }
    register_response = requests.post(register_url, json=register_payload)
    assert register_response.status_code == 422