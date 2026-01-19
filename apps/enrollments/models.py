"""apps.py
Mmodelo de usuarios con SQLAlchemy, incluyendo roles y autenticación básica.
"""

from sqlalchemy import Column, Integer, String, Enum, Boolean, Text, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

from core.database import Base

# Tabla intemedio estudiante -enrollment -course
class Enrollment(Base):
    __tablename__= "enrollment"
    student_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    course_id = Column(Integer, ForeignKey("course.id"), primary_key=True)
    completed = Column(Boolean, default=False, index=True)
    grade = Column(Float, default=0.00, index=True)

    student = relationship("user", back_populates="enrollment")
    course = relationship("course", back_populates="enrollment")