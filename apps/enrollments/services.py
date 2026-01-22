from typing import Optional

from fastapi import HTTPException
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from apps.enrollments.models import Enrollment
from apps.enrollments.schemas import EnrollmentCreate, EnrollmentUpdate


# Crear Enrollment
def create_enrollment(db: Session, student_id: int, course_id: int) -> Enrollment:
    db_enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.add(db_enrollment)
    try:
        db.commit()
        db.refresh(db_enrollment)
        return db_enrollment
    except Exception as e:
        db.rollback()
        print("ERROR REAL:", e)
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# Listar enrollments
def get_enrollments(student_id:int, db: Session, skip: int = 0, limit: int = 10) -> Optional[list[Enrollment]]:
    try:
        stmt = (select(Enrollment).where(student_id == Enrollment.student_id).offset(skip).limit(limit))
        return db.execute(stmt).scalars().all()
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(
            status_code=500,
            detail=str(e)
    )

