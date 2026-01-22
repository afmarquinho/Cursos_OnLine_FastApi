import logging

import requests

from apps.users.security import decode_access_token

BASE_URL = "http://127.0.0.1:8000/api/users"
token = ""
INVALID_TOKEN = "invalid_token"
headers = ""


def print_test(name: str) -> str:
    print(f"\n {name}\n" + "-" * 50)
#
# print_test("Usuario admin")
# def test_create_1():
#     payload = {"username": "user1", "email": "user1@example.com", "password": "UnaClave123*", "role": "admin"}
#     res = requests.post(f"{BASE_URL}/register", json=payload)
#     assert res.status_code == 201
#
# print_test("Usuario profesor")
# def test_create_2():
#     payload = {"username": "user2", "email": "user2@example.com", "password": "UnaClave123*", "role": "professor"}
#     res = requests.post(f"{BASE_URL}/register", json=payload)
#     assert res.status_code == 201
#
# print_test("Ususario profesor")
# def test_create_3():
#     payload = {"username": "user3", "email": "user3@example.com", "password": "UnaClave123*", "role": "professor"}
#     res = requests.post(f"{BASE_URL}/register", json=payload)
#     assert res.status_code == 201
#
# print_test("Usuario admin")
# def test_create_4():
#     payload = {"username": "user4", "email": "user4@example.com", "password": "UnaClave123*", "role": "admin"}
#     res = requests.post(f"{BASE_URL}/register", json=payload)
#     assert res.status_code == 201

# Login correcto, devuelve access token.
def test_login_success():
    # login correcto
    payload = {"email": "user1@example.com", "password":"UnaClave123*"}
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
    i = 0
    user_list = admin_res.json()
    for user in user_list:
        i +=1
        print(f"\n{i} - {user}")


#
# print_test("Prueba 2: Login incorrecto por password incorrecta")
# def test_login_unsuccess():
#     res = requests.post(f"{BASE_URL}/login",
#                         json={"email": "user2@example.com", "password":"UnaClave123"})
#
#     assert res.status_code == 401
#
#
# print_test("Prueba 3: Login incorrecto por falta de password")
# def test_login_unsuccess_2():
#     res = requests.post(f"{BASE_URL}/login",
#                         json={"email": "user2@example.com"})
#     assert res.status_code ==422
#
#
# print_test("Prueba 4: Login correcto y rol incorrecto diferente a admin")
# def test_login_unauthorized():
#     # login correcto
#     payload = {"email": "user3@example.com", "password":"UnaClave123*"}
#     res = requests.post(f"{BASE_URL}/login",
#                         json=payload
#                                  )
#     assert res.status_code == 200
#     assert res.json()["access_token"]
#     global token, headers
#     token = res.json()["access_token"]
#     headers = {"Authorization":f"Bearer {token}"}
#     # Rol Admin correcto
#     admin_res = requests.get(f"{BASE_URL}/get-all", headers=headers)
#     assert admin_res.status_code==403
#
# def test_get_all_students():
#     res = requests.get(f"{BASE_URL}/get-all-students", headers=headers)
#     print(f"Token: {token}")
#     assert res.status_code == 200
#     i = 0
#     student_list = res.json()
#     for student in student_list:
#         i += 1
#         print(f"\n{i} - {student}")