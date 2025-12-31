# main.py

from fastapi import FastAPI

from apps.users.router import router as user_router

# Crea la instancia principal de la aplicacion FastAPI,
# La APP serà usada por uvicorn para levantar el servidor

app = FastAPI(title="Course Management API", version="1.0.0",
              description="Backend REST con FASTAPI para gestionar cursos y estudiantes")


app.include_router(user_router)


# Endpoint de prueba para la ruta raiz
@app.get("/")
# Mensaje de confirmacion de la api funcionando
def root():
    return {"message": "Bienvenido a la Course Management API"}
