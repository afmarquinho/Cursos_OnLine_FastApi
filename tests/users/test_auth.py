# Se prueba la autenticaciòn or token vàlido
'''Ejecutar: -Desde la ràiz
Manual: python tests/users/test_auth.py
Usando pytest: Desde la consola tengo 4 opciones
Opciòn 1: pytest --> Ejecuta todos los tests
Opciòn 1.1 : pytest -v -s --> Ejecuta todos los tests e imprime los prints
Opcion 2: pytest tests/users --> Todos los tests en users
Opciòn 3: pytest tests/users/test_auth.py --> Todos los tests en el archivo
Opciòn 4: pytest tests/users/test_auth.py::test_token --> Ejecuta un tests especìfico
'''

from apps.users.security import decode_access_token

VALID_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3Iiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzY3NjU5ODg0fQ.K4tJV9azC382qz4GMOOz4B33dzPMkByFE5H33r3LMhk"
INVALID_TOKEN = "TOKEN"


def test_token_valid():
    try:
        payload = decode_access_token(VALID_TOKEN)
        print("TOKEN VÀLIDO")
        print(payload)
    except Exception as e:
        print("TOKEN INVÀLIDO")
        print(type(e).__name__, str(e))

def test_token_invalid():
    try:
        payload = decode_access_token(INVALID_TOKEN)
        print("TOKEN VÀLIDO")
        print(payload)
    except Exception as e:
        print("TOKEN INVÀLIDO")
        print(type(e).__name__, str(e))

if __name__ == "__main__":
    print("*** Token Vàlido ***")
    test_token_valid(VALID_TOKEN)

    print()
    print("*** Token Invàlido ***")
    test_token_invalid(INVALID_TOKEN)