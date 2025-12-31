from pydantic import BaseModel, EmailStr, Field, field_validator
from enum import Enum


# Enum de roles (igual que en SQLAlchemy)
class UserRole(str, Enum):
    admin = "admin"
    profesor = "profesor"
    estudiante = "estudiante"

# Base común
class UserBase(BaseModel):
    # Los tres punyos "..." indican que el campoes obliugatorio segun pydantic
    username: str = Field(..., min_length=3, max_length=50, description="Nombre de usuario único")
    email: EmailStr = Field(..., description="Correo electrónico válido")
    role: UserRole = Field(default=UserRole.estudiante, description="Rol del usuario")

    # Validación personalizada para username
    @field_validator("username")
    def no_spaces(cls, v):
        if " " in v:
            raise ValueError("El nombre de usuario no puede contener espacios")
        return v


# Crear usuario (incluye password en texto plano)
class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128, description="Contraseña segura")

    @field_validator("password")
    def strong_password(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError("La contraseña debe contener al menos una letra mayúscula")
        if not any(c.isdigit() for c in v):
            raise ValueError("La contraseña debe contener al menos un número")
        return v

class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="Correo electrónico válido")
    password: str = Field(..., min_length=8, max_length=128, description="Contraseña segura")

    def strong_password(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError("La contraseña debe contener al menos una letra mayúscula")
        if not any(c.isdigit() for c in v):
            raise ValueError("La contraseña debe contener al menos un número")
        return v


# Actualizar usuario (campos opcionales)
class UserUpdate(BaseModel):
    username: str | None = Field(None, min_length=3, max_length=50)
    email: EmailStr | None = None
    role: UserRole | None = None
    password: str | None = Field(None, min_length=8, max_length=128)

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


# Leer usuario (respuesta al cliente)
class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
