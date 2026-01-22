import requests

BASE_URL = "http://127.0.0.1:8000/api"
token = ""
INVALID_TOKEN = "invalid_token"
headers = ""


# Login correcto, devuelve access token.
def test_login_success():
    # login correcto con usuario rol profesor
    payload = {"email": "user2@example.com", "password": "UnaClave123*"}
    res = requests.post(f"{BASE_URL}/users/login",
                        json=payload
                        )
    assert res.status_code == 200
    assert res.json()["access_token"]
    global token, headers
    token = res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}


# def test_create_course_1():
#     payload = {"title": "Django de cero a avanzado + DRF, Flask y FastApi",
#                "description": "Domina el lenguaje nùmero uno en el mundo"}
#
#     res = requests.post(f"{BASE_URL}/courses/create",
#                         json=payload, headers=headers)
#     assert res.status_code == 201
#
# def test_create_course_2():
#     payload = {
#         "title": "Introducción a Django",
#         "description": "Curso práctico para aprender a crear aplicaciones web con Django, incluyendo modelos, vistas y plantillas."
#     }
#
#     res = requests.post(f"{BASE_URL}/courses/create",
#                         json=payload, headers=headers)
#     assert res.status_code == 201
#
#
# def test_create_course_3():
#     payload = {
#         "title": "Bases de Datos con SQL",
#         "description": "Aprende a diseñar, consultar y optimizar bases de datos relacionales utilizando SQL y buenas prácticas."
#     }
#     res = requests.post(f"{BASE_URL}/courses/create",
#                         json=payload, headers=headers)
#     assert res.status_code == 201
#
# def test_get_all():
#     res = requests.get(f"{BASE_URL}/courses/get-all",
#                         headers=headers)
#     assert res.status_code == 200
#     for course in res.json():
#         print(course)

# def test_get_course_by_id():
#     res = requests.get(f"{BASE_URL}/courses/get-one/3", headers=headers)
#     assert res.status_code == 200
#     print(f"Curso: {res.json()}")


# # Test de rutas para lesson
# def test_create_lesson_forbidden_role():
#     payload = {"title": "Fundamentos de Python", "professor_id": 1}
#     res = requests.post(f"{BASE_URL}/courses/lesson/create", json=payload, headers=headers)
#
#     assert res.status_code == 403
#
#
# def test_create_lesson_successful_1():
#     payload = {"title": "Funciones", "professor_id": 2}
#     res = requests.post(f"{BASE_URL}/courses/lesson/create", json=payload, headers=headers)
#
#     assert res.status_code == 201
#
# def test_create_lesson_successful_2():
#     payload = {"title": "Conexiones a la base de datos", "professor_id": 2}
#     res = requests.post(f"{BASE_URL}/courses/lesson/create", json=payload, headers=headers)
#
#     assert res.status_code == 201
#
# def test_create_lesson_successful_3():
#     payload = {"title": "Pool de conexiones a la bbdd", "professor_id": 2}
#     res = requests.post(f"{BASE_URL}/courses/lesson/create", json=payload, headers=headers)
#
#     assert res.status_code == 201
#
# def test_create_lesson_successful_4():
#     payload = {"title": "Pràctica 1", "professor_id": 2}
#     res = requests.post(f"{BASE_URL}/courses/lesson/create", json=payload, headers=headers)
#
#     assert res.status_code == 201
#
# def test_create_lesson_successful_5():
#     payload = {"title": "Pràctica 2", "professor_id": 2}
#     res = requests.post(f"{BASE_URL}/courses/lesson/create", json=payload, headers=headers)
#
#     assert res.status_code == 201

def test_get_all_lessons():
    res = requests.get(f"{BASE_URL}/courses/lesson/get-all", headers=headers)
    assert res.status_code == 200
    for lesson in res.json():
        print(lesson)


#
# def test_assign_lesson_to_course():
#     res = requests.post(f"{BASE_URL}/courses/2/lesson/1", headers=headers)
#     assert res.status_code == 201
