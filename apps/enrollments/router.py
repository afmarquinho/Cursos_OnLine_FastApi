from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from apps.enrollments.schemas import EnrollmentOut
from apps.enrollments import services
from apps.users.dependencies import role_required

from core.database import get_db

router = APIRouter(prefix='/api/enrollments', tags=['Enrollments'])


@router.post('/{student_id}/course/{course_id}', response_model=EnrollmentOut, status_code=201)
def create(student_id:int, course_id:int, db: Session = Depends(get_db),  _: dict = Depends(role_required(["student"]))):
    db_enrollment = services.create_enrollment(db, student_id, course_id)
    return db_enrollment

@router.get("/get-all/{student_id}", response_model=List[EnrollmentOut], status_code=200)
async def get_all(student_id:int, db: Session = Depends(get_db), _:dict=Depends(role_required(["student"]))):
        enrollment_list = services.get_enrollments( student_id, db)
        if not enrollment_list:
            raise HTTPException(status_code=404, detail="Cursos no encontrados")
        return enrollment_list