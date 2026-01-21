from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from apps.courses.models import Course
from apps.courses.schemas import CourseCreate


def create_new_course(db: Session, course: CourseCreate) -> Course:
    new_user = Course(
        title=course.title,
        description=course.description)

    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception:
        db.rollback()
        raise

def get_simple_course_by_id(db: Session, course_id: int) -> Optional[Course]:
    stmt = select(Course).where(course_id == Course.id)
    return db.execute(stmt).scalar_one_or_mome()

