# # Se prueba la autenticaciòn or token vàlido
# '''Ejecutar: -Desde la ràiz
# Manual: python tests/users/test_auth.py
# Usando pytest: Desde la consola tengo 4 opciones
# Opciòn 1: pytest --> Ejecuta todos los tests
# Opciòn 1.1 : pytest -v -s --> Ejecuta todos los tests e imprime los prints
# Opcion 2: --> Todos los tests en users
# Opciòn 3: pytest tests/users/test_auth.py --> Todos los tests en el archivo
# Opciòn 4: pytest tests/users/test_auth.py::test_token --> Ejecuta un tests especìfico
# '''
# from logging import raiseExceptions
#
# import pytest
# from fastapi import HTTPException
#
# from apps.users.dependencies import get_current_user
# from apps.users.security import hash_password, verify_password, create_access_token
#
# pwd:str = "12345"
# hash_pwd:str =  ""
# wrong_pwd:str = "1234"
# valid_token = ""
# INVALID_TOKEN = "INVALID TOKEN"
#
# def test_hash_pwd():
#     global hash_pwd
#     hash_pwd = hash_password(pwd)
#     print(hash_pwd)
#
# def test_valid_pwd():
#     is_valid = verify_password(pwd, hash_pwd)
#     print(f"\nEl password es vàlido: {is_valid}")
#
# def test_wrong_pwd():
#     is_valid = verify_password(wrong_pwd, hash_pwd)
#     print(f"\nEl password es invàlido: {is_valid}")
#
# def test_create_access_token():
#     data: dict = {"sub": "1", "username": "user", "role": "admin"}
#     global valid_token
#     valid_token = create_access_token(data)
#     print(f"\nToken Generado: {valid_token}")
#
# def test_valid_token():
#     is_valid = get_current_user(valid_token)
#     print(f"\nToken validado correctamente, datos del usuario: {is_valid}")
#
#
# def test_invalid_token():
#     with pytest.raises(Exception):
#         is_valid = get_current_user(INVALID_TOKEN)
#         print(f"\nToken invalidado: {'No User' if is_valid is None else is_valid}")
#
#
#
#
#
#
#
