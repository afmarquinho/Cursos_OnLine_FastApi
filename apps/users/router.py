from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from apps.users import schemas
from apps.users import services
from apps.users.dependencies import role_required
from apps.users.services import get_users
from apps.users.students.schemas import StudentOut
from apps.users.students.services import get_students
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

    access_token = services.generate_token(user.id, user.role.value, user.username, user.is_active)

    return {
        "access_token": access_token, "token_type":"bearer"
    }

# Rutas solo para admins, obtiene todos los usuarios y estudiantes
@router.get("/get-all", response_model=List[schemas.UserOut], status_code=200)
async def get_all(db: Session = Depends(get_db), _:dict=Depends(role_required(["admin", "professor"]))):
        user_list = get_users(db)
        if not user_list:
            raise HTTPException(status_code=404, detail="Usuarios no encontrados")
        return user_list

@router.get("/get-all-students", response_model=List[StudentOut], status_code=200)
async def get_all_students (db: Session = Depends(get_db), _:dict=Depends(role_required(["admin"]))):
        student_list = get_students(db)
        if not student_list:
            raise HTTPException(status_code=404, detail="Usuarios no encontrados")
        return student_list
