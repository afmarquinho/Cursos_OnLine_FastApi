# main.py
import logging

from fastapi import FastAPI

from apps.users.router import router as user_router
from apps.users.students.router import router as student_router
from apps.courses.router import router as course_router
from apps.enrollments.router import router as enrollment_router

from core.logging_config import setup_logging
import core.models  # fuerza el registro de todos los modelos

# Crea la instancia principal de la aplicacion FastAPI,
# La APP serà usada por uvicorn para levantar el servidor

app = FastAPI(title="Course Management API", version="1.0.0",
              description="Backend REST con FASTAPI para gestionar cursos y estudiantes")

# Inicializa el log para hacer seguimiento a los logs de manera global
setup_logging()
app.include_router(user_router)
app.include_router(student_router)
app.include_router(course_router)
app.include_router(enrollment_router)




# Endpoint de prueba para la ruta raiz
@app.get("/")
# Mensaje de confirmacion de la api funcionando
def root():
    logger = logging.getLogger(__name__)
    logger.info("Endpoint raiz llamado")
    return {"message": "Bienvenido a la Course Management API"}
