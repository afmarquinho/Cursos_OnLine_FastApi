from typing import Optional

from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from apps.users.models import User
from apps.users.schemas import UserCreate, UserUpdate
from apps.users.security import hash_password, verify_password, create_access_token


# Crear Usuario
def create_user(db: Session, user: UserCreate) -> User:
    hashed_pw = hash_password(user.password)
    db_user = User(username=user.username,
                   email=user.email,
                   hashed_password=hashed_pw,
                   role=user.role
                   )
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception:
        db.rollback()
        raise


# Obtener usuario por ID
def get_user(db: Session, user_id: int) -> Optional[User]:
    stmt = select(User).where(user_id == User.id)
    return db.execute(stmt).scalar_one_or_none()


# Obtener usuario por email
def get_user_by_email(db: Session, email: str) -> Optional[User]:
    stmt = select(User).where(User.emai==email)
    return db.execute(stmt).scalar_one_or_none()


# Listar usuarios
def get_users(db: Session, skip: int = 0, limit: int = 10) -> list[User]:
    stmt = (select(User).offset(skip).limit(limit))
    return db.execute(stmt).scalars().all()


# Actualizar usuario
def update_user(db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
    db_user = get_user(db, user_id)
    if not db_user:
        return None

    if user_update.username is not None:
        db_user.username = user_update.username
    if user_update.email is not None:
        db_user.email = user_update.email
    if user_update.role is not None:
        db_user.role = user_update.role
    if user_update.password is not None:
        db_user.hashed_password = hash_password(user_update.password)

    try:
        db.commit()
        db.refresh(db_user)
    except Exception:
        db.rollback()
        raise


# Eliminar usuario


def delete_user(db: Session, user_id: int) -> bool:
    stmt = select(User).where(User.id == user_id)
    db_user = db.execute(stmt).scalar_one_or_none()

    if not db_user:
        return False

    db.delete(db_user)
    db.commit()
    return True



def authenticate_user(
    db: Session,
    email: str,
    password: str
) -> Optional[User]:
    stmt = select(User).where(User.email == email)
    user = db.execute(stmt).scalar_one_or_none()

    if not user or not verify_password(password, user.hashed_password):
        return None

    return user


def generate_token(user: User):
    return create_access_token({"sub": user.email, "role": user.role.value})
