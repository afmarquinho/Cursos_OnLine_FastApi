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
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.estudiante, nullable=False)
    is_active = Column(Boolean, default=True, index=True)

    enrollment = relationship("Enrollment", back_populates="users")


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50), unique=True, nullable=False, index=True)
    description = Column(Text)
    is_active = Column(Boolean, default=True, index=True)

    enrollment = relationship("Enrollment", back_populates="courses")


class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50), unique=True, nullable=False, index=True)

user_lesson = Table(
    "user_lesson",
    Base.metadata,
    Column("student.id", ForeignKey("users.id"), primary_key = True),
    Column("course.id", ForeignKey("courses.id"), primary_key = True)
)

# Tabla intemedio estudiante -enrollment -course
class Enrollment(Base):
    __tablename__= "enrollments"
    student_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), primary_key=True)
    completed = Column(Boolean, default=False, index=True)
    grade = Column(Float, default=0.00, index=True)

    student = relationship("User", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")