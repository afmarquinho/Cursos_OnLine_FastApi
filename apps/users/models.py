"""apps.py
Mmodelo de usuarios con SQLAlchemy, incluyendo roles y autenticación básica.
"""
import enum

from sqlalchemy import Column, Integer, String, Enum, Boolean, Text, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

from core.database import Base



class UserRole(enum.Enum):
    admin = "admin"
    professor = "professor"

class StudentRole(enum.Enum):
    student = "student"

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.professor, nullable=False)
    is_active = Column(Boolean, default=True, index=True)

    # Relación con Lesson parea profesores
    lessons = relationship("Lesson", back_populates="user")

    def __repr__(self):
        return (
            f"<User(id={self.id}, "
            f"username='{self.username}', "
            f"email='{self.email}', "
            f"role='{self.role.name}', "
            f"is_active={self.is_active})>"
        )

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    role = Column(Enum(StudentRole), default=StudentRole.student, nullable=False)
    is_active = Column(Boolean, default=True, index=True)

    enrollment = relationship("Enrollment", back_populates="student")
