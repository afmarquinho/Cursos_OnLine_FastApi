from pydantic import BaseModel, EmailStr, Field, field_validator
from enum import Enum


# Enum de roles (igual que en SQLAlchemy)
class StudentRole(str, Enum):
    student = "student"

# Base común
class StudentBase(BaseModel):
    # Los tres punTos "..." indican que el campoes obliugatorio segun pydantic
    username: str = Field(..., min_length=3, max_length=50, description="Nombre de usuario único")
    email: EmailStr = Field(..., description="Correo electrónico válido")


    # Validación personalizada para username
    @field_validator("username")
    def no_spaces(cls, v):
        if " " in v:
            raise ValueError("El nombre de usuario no puede contener espacios")
        return v


# Crear estudiante (incluye password en texto plano)
class StudentCreate(StudentBase):
    password: str = Field(..., min_length=8, max_length=128, description="Contraseña segura")

    @field_validator("password")
    def strong_password(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError("La contraseña debe contener al menos una letra mayúscula")
        if not any(c.isdigit() for c in v):
            raise ValueError("La contraseña debe contener al menos un número")
        return v


class StudentLogin(BaseModel):
    email: EmailStr = Field(..., description="Correo electrónico válido")
    password: str = Field(..., min_length=8, max_length=128, description="Contraseña segura")


# Actualizar usuario (campos opcionales)
class StudentUpdate(BaseModel):
    username: str | None = Field(None, min_length=3, max_length=50)
    email: EmailStr | None = None
    role: StudentRole | None = None
    password: str | None = Field(None, min_length=8, max_length=128)
    diabled: bool | None = Field(None, description="Indica si el usuario está deshabilitado")

    @field_validator("username")
    def no_spaces(cls, v):
        if v and " " in v:
            raise ValueError("El nombre de usuario no puede contener espacios")
        return v

    @field_validator("password")
    def strong_password(cls, v):
        if v:
            if not any(c.isupper() for c in v):
                raise ValueError("La contraseña debe contener al menos una letra mayúscula")
            if not any(c.isdigit() for c in v):
                raise ValueError("La contraseña debe contener al menos un número")
        return v


# class LoginResponse(BaseModel):
#     access_token: str

# Modelo para el token
class Token(BaseModel):
    access_token: str
    token_type: str

# Modelo del token decodificado
class CurrentStudent(BaseModel):
    Student_id: int
    role: str
    username: str
    is_active:bool


# Leer usuario (respuesta al cliente)
class StudentOut(StudentBase):
    role:str
    is_active:bool
    id: int

    model_config = {'from_attributes': True}
