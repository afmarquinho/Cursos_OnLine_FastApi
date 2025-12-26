import os

import pymysql
from alembic import command
from alembic.config import Config
from dotenv import load_dotenv

# Cargar las veriables de entorno
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


# Verifica si existe la base datos y is existe la tabla de alembic_version
def limpiar_alembic_version():
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""SHOW TABLES LIKE 'alembic_version'
        """)
        existe = cursor.fetchone()
        if existe:
            print("Tabla alembic version encontrada. OK.")
        else:
            print("No existe tabla alembic_version. Continuando...")
        conn.close()
    except Exception as e:
        print("Error verificando alembic_version", e)


# Ejecutar migraciòn automàtica
def ejecutar_migracion():
    alembic_cfg = Config("alembic.ini")
    print("Generando revisiòn autogenerada...")
    command.revision(alembic_cfg, autogenerate=True, message="init usuarios")

    print("Aplicando miugraciones (upgrade head)...")
    command.upgrade(alembic_cfg, "head")
    print("Migraciòn aplicada correctamente.")

if __name__ == "__main__":
    limpiar_alembic_version()
    ejecutar_migracion()

    