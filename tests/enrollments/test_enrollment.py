import pytest
import requests

from apps.users.dependencies import get_current_user
from apps.users.security import decode_access_token

BASE_URL = "http://127.0.0.1:8000/api"
token = ""
INVALID_TOKEN = "invalid_token"
headers = ""
current_user=""
student_id=""

def test_login_success():
    # login correcto
    payload = {"email": "student4@example.com", "password":"UnaClave123*"}
    res = requests.post(f"{BASE_URL}/students/login",
                        json=payload
                                 )
    assert res.status_code == 200
    assert res.json()["access_token"]
    global token, headers, current_user, student_id
    token = res.json()["access_token"]
    headers = {"Authorization":f"Bearer {token}"}
    current_user = decode_access_token(token)

    # student_id = current_user["sub"]
    student_id = int(current_user.get("sub"))


def test_new_enrollment():
    course_id= 2
    res = requests.post(f"{BASE_URL}/enrollments/{student_id}/course/{course_id}", headers=headers)
    print("STATUS:", res.status_code)
    print("BODY:", res.text)
    assert res.status_code == 201

def test_new_enrollment_2():
    course_id= 3
    res = requests.post(f"{BASE_URL}/enrollments/{student_id}/course/{course_id}", headers=headers)

    assert res.status_code == 201

def test_new_enrollment_3():
    course_id= 1
    res = requests.post(f"{BASE_URL}/enrollments/{student_id}/course/{course_id}", headers=headers)

    assert res.status_code == 201

def test_get_courses():
    res = requests.get(f"{BASE_URL}/enrollments/get-all/{student_id}", headers=headers)
    courses_list = res.json()
    for course in courses_list:
        print(course)
    assert res.status_code == 200

