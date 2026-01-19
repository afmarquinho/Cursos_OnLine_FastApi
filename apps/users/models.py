"""apps.py
Mmodelo de usuarios con SQLAlchemy, incluyendo roles y autenticación básica.
"""
import enum

from sqlalchemy import Column, Integer, String, Enum, Boolean, Text, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

from core.database import Base


class UserRole(enum.Enum):
    admin = "admin"
    profesor = "profesor"
    estudiante = "estudiante"

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.estudiante, nullable=False)
    is_active = Column(Boolean, default=True, index=True)

    enrollment = relationship("enrollment", back_populates="user")