from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from apps.users import schemas
from apps.users import services
from core.database import get_db

router = APIRouter(prefix='/api/users', tags=['Users'])


@router.post('/register', response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = services.create_user(db, user)
    return db_user


@router.post("/login", response_model=schemas.UserOut, status_code=201)
def login(form_data: schemas.UserCreate, db: Session = Depends(get_db)):
    user = services.authenticate_user(db, form_data.email, form_data.password)

    if not user:
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    token = generate_token(user)
    return {"access_token": token, "token_type": "bearer"}
