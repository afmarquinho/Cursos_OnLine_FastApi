from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from apps.users.services import generate_token
from apps.users.students import schemas
from apps.users.students import services
from apps.users.dependencies import check_admin, role_required
from core.database import get_db

router = APIRouter(prefix='/api/students', tags=['Students'])


@router.post('/register', response_model=schemas.StudentOut, status_code=201)
def register(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = services.create_student(db, student)
    return db_student


@router.post("/login", response_model=schemas.Token, status_code=200)
async def login(form_data: schemas.StudentLogin, db: Session = Depends(get_db)):
    student = services.authenticate_student(db, form_data.email, form_data.password)
    if not student:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    access_token = generate_token(student.id, student.role.value, student.username, student.is_active)

    return {
        "access_token": access_token, "token_type":"bearer"
    }


