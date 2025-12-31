"""database.py
Confirguraciòn  de la base de datos
"""

import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables desde .env

class Settings:
    PROJECT_NAME: str = "Course Management API"
    VERSION: str = "1.0.0"
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")

    """Funcion que retorna el string de conexiòn a la bbdd """

    @property
    def DATABASE_URL(self):
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
