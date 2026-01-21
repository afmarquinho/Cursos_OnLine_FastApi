from typing import Optional

from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from apps.users.models import Student
from apps.users.security import verify_password, hash_password
from apps.users.students.schemas import StudentCreate, StudentUpdate


# Obtener usuario por email
def get_student_by_email(db: Session, email: str) -> Optional[Student]:
    stmt = select(Student).where(Student.email == email)
    return db.execute(stmt).scalar_one_or_none()


# Autenticaciòn
def authenticate_student(
        db: Session,
        email: str,
        password: str
) -> Optional[Student]:
    student = get_student_by_email(db, email)

    if not student or not verify_password(password, student.password):
        return None

    return student


# Crear Usuario
def create_student(db: Session, student: StudentCreate) -> Student:
    hashed_pw = hash_password(student.password)
    db_student = Student(username=student.username,
                         email=student.email,
                         password=hashed_pw
                         )
    db.add(db_student)
    try:
        db.commit()
        db.refresh(db_student)
        return db_student
    except Exception:
        db.rollback()
        raise


# Obtener usuario por ID
def get_student_by_id(db: Session, student_id: int) -> Optional[Student]:
    stmt = select(Student).where(student_id == Student.id)
    return db.execute(stmt).scalar_one_or_none()


# Listar usuarios
def get_students(db: Session, skip: int = 0, limit: int = 10) -> Optional[list[Student]]:
    stmt = (select(Student).offset(skip).limit(limit))
    return db.execute(stmt).scalars().all()


# Actualizar usuario
def update_students(db: Session, student_id: int, student_update: StudentUpdate) -> Optional[Student]:
    db_student = get_student_by_id(db, student_id)
    if not db_student:
        return None

    if student_update.username is not None:
        db_student.username = student_update.username
    if student_update.email is not None:
        db_student.email = student_update.email
    if student_update.role is not None:
        db_student.role = student_update.role
    if student_update.password is not None:
        db_student.password = hash_password(student_update.password)

    try:
        db.commit()
        db.refresh(db_student)
    except Exception:
        db.rollback()
        raise


# Eliminar estudiante
def delete_student(db: Session, student_id: int) -> bool:
    db_student = get_student_by_id(db, student_id)

    if not db_student:
        return False

    db.delete(db_student)
    db.commit()
    return True

#
# def generate_token(student_id: int, role: str, username: str, is_active: bool):
#     return create_access_token({"sub": str(student_id),
#                                 "role": role,
#                                 "username": username,
#                                 "is_active": is_active})
