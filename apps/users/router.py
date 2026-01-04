from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from apps.users import schemas
from apps.users import services
from core.database import get_db

router = APIRouter(prefix='/api/users', tags=['Users'])


@router.post('/register', response_model=schemas.UserOut, status_code=201)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = services.create_user(db, user)
    return db_user


@router.post("/login", response_model=schemas.LoginResponse, status_code=200)
def login(form_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = services.authenticate_user(db, form_data.email, form_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = services.generate_token(user.id, user.role)

    return {
        "username": user.username,
        "token": token
    }



@router.get("/get-all", response_model=schemas.UserOut, status_code=200)
def get_all(db: Session = Depends(get_db)):
    user_list = services.get_users(db)
    if not user_list:
        raise HTTPException(status_code=404, detail="Usuarios no encontrados")
    return user_list
