import logging

import requests

logger = logging.getLogger(__name__)
logger.debug("Endpoint raiz llamado")

BASE_URL = "http://127.0.0.1:8000/api/users"
token=""
INVALID_TOKEN="invalid_token"
headers=""


def print_test(name:str) -> str:
    print(f"\n {name}\n" + "-"*50)


# 1. Login correcto, devuelve access token.
print_test("Prueba 1: Login correcto y admin correcto")
def test_login_success():
    # login correcto
    payload = {"email": "user2@example.com", "password":"UnaClave123*"}
    res = requests.post(f"{BASE_URL}/login",
                        json=payload
                                 )
    assert res.status_code == 200
    assert res.json()["access_token"]
    global token, headers
    token = res.json()["access_token"]
    headers = {"Authorization":f"Bearer {token}"}
    # Rol Admin correcto
    admin_res = requests.get(f"{BASE_URL}/get-all", headers=headers)
    assert admin_res.status_code==200
    i = 0
    user_list = admin_res.json()
    for user in user_list:
        i +=1
        print(f"\n{i} - {user}")



print_test("Prueba 2: Login incorrecto por password incorrecta")
def test_login_unsuccess():
    res = requests.post(f"{BASE_URL}/login",
                        json={"email": "user2@example.com", "password":"UnaClave123"})

    assert res.status_code == 401


print_test("Prueba 3: Login incorrecto por falta de password")
def test_login_unsuccess_2():
    res = requests.post(f"{BASE_URL}/login",
                        json={"email": "user2@example.com"})
    assert res.status_code ==422


print_test("Prueba 4: Login correcto y rol incorrecto diferente a admin")
def test_login_unauthorized():
    # login correcto
    payload = {"email": "user5@example.com", "password":"UnaClave123*"}
    res = requests.post(f"{BASE_URL}/login",
                        json=payload
                                 )
    assert res.status_code == 200
    assert res.json()["access_token"]
    global token, headers
    token = res.json()["access_token"]
    headers = {"Authorization":f"Bearer {token}"}
    # Rol Admin correcto
    admin_res = requests.get(f"{BASE_URL}/get-all", headers=headers)
    assert admin_res.status_code==403

