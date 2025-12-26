"""database.py
Conexiòn a la base de datos"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from core.config import settings

# Crear motor de conexión
engine = create_engine(settings.DATABASE_URL,  echo=True)

# Sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()

# Dependencia para obtener sesión en endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Prueba ràpida de conexiòn: ejecutar con "python database.py"
if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            print("Conexiòn exitosa a MySql")
    except Exception as e:
            print("Error al conectar la BBDD: ", e)