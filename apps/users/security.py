from datetime import datetime, timedelta, timezone
from http.client import HTTPException

import bcrypt
from fastapi.openapi.utils import status_code_ranges
from jose import jwt, JWTError
from core.config import settings


def hash_password(plain_password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_password.encode("utf-8"), salt)
    return hashed.decode("utf-8")

def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


def create_access_token(data:dict):
    to_encode = data.copy()
    expire = (datetime.now(timezone.utc) +
              timedelta(minutes=int(settings.JWT_ACCESS_TOKEN_EXIPIRE_MINUTES)))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET,
                      algorithm=settings.JWT_ALGORITHM)

def decode_access_token(token:str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET,
                             algorithms=[settings.JWT_ALGORITHM])

        return payload
    except JWTError:
        raise HTTPException(status_code=401 , detail="Token in`valido o expirado")
