from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from apps.users import schemas
from apps.users import services
from apps.users.dependencies import check_admin
from core.database import get_db

router = APIRouter(prefix='/api/users', tags=['Users'])


@router.post('/register', response_model=schemas.UserOut, status_code=201)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = services.create_user(db, user)
    return db_user


@router.post("/login", response_model=schemas.Token, status_code=200)
async def login(form_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = services.authenticate_user(db, form_data.email, form_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    access_token = services.generate_token(user.id, user.role.value, user.username)

    return {
        "access_token": access_token, "token_type":"bearer"
    }

# Ruta solo para admins, obtiene todos los usuarios
@router.get("/get-all", response_model=List[schemas.UserOut], status_code=200)
async def get_all(db: Session = Depends(get_db), _:dict=Depends(check_admin)):
        user_list = services.get_users(db)
        if not user_list:
            raise HTTPException(status_code=404, detail="Usuarios no encontrados")
        return user_list
