from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from apps.courses import schemas
from apps.courses import services
from apps.users.dependencies import role_required

from core.database import get_db

router = APIRouter(prefix='/api/courses', tags=['Course'])


@router.post('/create', response_model=schemas.CourseOut, status_code=201)
def create(form_data: schemas.CourseCreate, db: Session = Depends(get_db),
           _: dict = Depends(role_required(["professor"]))):
    db_course = services.create_new_course(db, form_data)
    return db_course


@router.get("/get-all", response_model=List[schemas.CourseOut], status_code=200)
async def get_course(db: Session = Depends(get_db), _: dict = Depends(role_required(["professor"]))):
    course_list = services.get_courses(db)

    if not course_list:
        raise HTTPException(status_code=404, detail="Cursos no encontrados")
    return course_list


@router.get("/get-one/{course_id}", response_model=schemas.CourseOut, status_code=200)
async def get_by_id(
        course_id: int,
        db: Session = Depends(get_db),
        _: dict = Depends(role_required(["professor"]))
):
    course = services.get_simple_course_by_id(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return course


@router.post('/lesson/create', response_model=schemas.LessonOut, status_code=201)
def create_lesson(form_data: schemas.LessonCreate, db: Session = Depends(get_db),
                  _: dict = Depends(role_required(["professor"]))):
    db_lesson = services.create_new_lesson(db, form_data)
    return db_lesson


@router.get('/lesson/get-all', response_model=List[schemas.LessonOut], status_code=200)
def get_all_lesson(db: Session = Depends(get_db),
                   _: dict = Depends(role_required(["professor"]))):
    db_lesson = services.get_lessons(db)
    return (db_lesson)


@router.get("/lesson/{lesson_id}", response_model=schemas.LessonOut, status_code=200)
def get_lesson_by_id(lesson_id: int, db: Session = Depends(get_db),
                     _: dict = Depends(role_required(["professor"]))):
    db_lesson = services.get_lesson_by_id(db, lesson_id)
    return db_lesson


@router.post('/{course_id}/lesson/{lesson_id}', response_model=dict, status_code=201)
def assign_lesson_to_course(course_id: int, lesson_id: int, db: Session = Depends(get_db),
                            _: dict = Depends(role_required(["professor"]))):
    course = services.get_simple_course_by_id(db, course_id)
    lesson = services.get_lesson_by_id(db, lesson_id)

    if not course or not lesson:
        raise HTTPException(
            status_code=404,
            detail="Curso o lecciòn no encontrada"
        )

    course.lessons.append(lesson)
    db.commit()
    return {"msg": f"Lecciòn: {lesson.title} asignada al curso {course.title}"}
