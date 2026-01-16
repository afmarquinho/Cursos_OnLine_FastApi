# main.py
import logging

from fastapi import FastAPI

from apps.users.router import router as user_router
from core.logging_config import setup_logging

# Crea la instancia principal de la aplicacion FastAPI,
# La APP serà usada por uvicorn para levantar el servidor

app = FastAPI(title="Course Management API", version="1.0.0",
              description="Backend REST con FASTAPI para gestionar cursos y estudiantes")

# Inicializa el log para hacer se3guimiento a los logs de manera global
setup_logging()

app.include_router(user_router)


# Endpoint de prueba para la ruta raiz
@app.get("/")
# Mensaje de confirmacion de la api funcionando
def root():
    logger = logging.getLogger(__name__)
    logger.info("Endpoint raiz llamado")
    return {"message": "Bienvenido a la Course Management API"}
