from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from apps.courses.models import Course, Lesson
from apps.courses.schemas import CourseCreate, LessonCreate
from apps.users.schemas import UserOut
from apps.users.services import get_user_by_id


def create_new_course(db: Session, course: CourseCreate) -> Course:
    new_course = Course(
        title=course.title,
        description=course.description)

    db.add(new_course)
    try:
        db.commit()
        db.refresh(new_course)
        return new_course
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al crear el curso"
        )

def get_courses(db:Session, skip: int = 0, limit: int = 10) -> Optional[list[Course]]:
    stmt = select(Course).offset(skip).limit(limit)
    return db.execute(stmt).scalars().all()

def get_simple_course_by_id(db: Session, course_id: int) -> Optional[Course]:
    stmt = select(Course).where(course_id == Course.id)
    return db.execute(stmt).scalar_one_or_none()



#
# def get_full_course_by_id(db: Session, course_id: int) -> Optional[Course]:
#     stmt = select(Course).where(course_id == Course.id)
#     return db.execute(stmt).scalar_one_or_mome()

from fastapi import HTTPException, status

# Servicios para lecciones
def create_new_lesson(db: Session, lesson: LessonCreate) -> Lesson:
    # Buscar el usuario por id y verificar que sea de rol profesor
    user: UserOut | None = get_user_by_id(db, lesson.professor_id)
    print(f"\n USUARIO: {user}\n")
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profesor no encontrado"
        )
    if user.role.value != "professor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No está permitido crear lecciones, el usuario no es profesor"
        )

    new_lesson = Lesson(title=lesson.title, professor_id=lesson.professor_id)

    db.add(new_lesson)
    try:
        db.commit()
        db.refresh(new_lesson)
        return new_lesson
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al crear la lección"
        )

def get_lessons(db:Session, skip: int = 0, limit: int = 10) -> Optional[list[Lesson]]:
    stmt = select(Lesson).offset(skip).limit(limit)
    return db.execute(stmt).scalars().all()

def get_lesson_by_id(db: Session, lesson_id: int) -> Optional[Lesson]:
    stmt = select(Lesson).where(lesson_id == Lesson.id)
    return db.execute(stmt).scalar_one_or_none()
