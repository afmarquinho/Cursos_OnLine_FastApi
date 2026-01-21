import requests

BASE_URL = "http://127.0.0.1:8000/api/students"
token = ""
INVALID_TOKEN = "invalid_token"
headers = ""


def print_test(name: str) -> str:
    print(f"\n {name}\n" + "-" * 50)


def test_create_1():
    payload = {"username": "student3", "email": "student3@example.com", "password": "UnaClave123*"}
    res = requests.post(f"{BASE_URL}/register", json=payload)
    assert res.status_code == 201


def test_create_2():
    payload = {"username": "student4", "email": "student4@example.com", "password": "UnaClave123*"}
    res = requests.post(f"{BASE_URL}/register", json=payload)
    assert res.status_code == 201


# Login correcto, devuelve access token.

def test_login_success():
    # login correcto
    payload = {"email": "student1@example.com", "password":"UnaClave123*"}
    res = requests.post(f"{BASE_URL}/login",
                        json=payload
                                 )
    assert res.status_code == 200
    assert res.json()["access_token"]
    global token, headers
    token = res.json()["access_token"]
    headers = {"Authorization":f"Bearer {token}"}
    print(f"Token: {token}")
    # Rol Admin correcto


def test_login_unsuccess():
    res = requests.post(f"{BASE_URL}/login",
                        json={"email": "student2@example.com", "password":"UnaClave123"})

    assert res.status_code == 401


def test_login_unsuccess_2():
    res = requests.post(f"{BASE_URL}/login",
                        json={"email": "student2@example.com"})
    assert res.status_code ==422



