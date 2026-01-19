"""apps.py
Mmodelo de usuarios con SQLAlchemy, incluyendo roles y autenticación básica.
"""
from sqlalchemy import Column, Integer, String, Enum, Boolean, Text, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

from core.database import Base

class Course(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50), unique=True, nullable=False, index=True)
    description = Column(Text)
    is_active = Column(Boolean, default=True, index=True)

    enrollment = relationship("Enrollment", back_populates="courses")


class Lesson(Base):
    __tablename__ = "lesson"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50), unique=True, nullable=False, index=True)


course_lesson = Table(
    "course_lesson",
    Base.metadata,
    Column("lesson_id", ForeignKey("lesson.id"), primary_key = True),
    Column("course_id", ForeignKey("course.id"), primary_key = True)
)
