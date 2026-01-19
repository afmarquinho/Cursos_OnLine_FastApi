from pydantic import BaseModel, Field, field_validator


# Esquemas para cursos

# Base común
class CourseBase(BaseModel):
    # Los tres punyos "..." indican que el campoes obliugatorio segun pydantic
    title: str = Field(..., min_length=5, max_length=50, description="Nombre del curso")
    description: str = Field(..., min_length=10, description="Descripciòn del curso")


# Crear curso
class CourseCreate(CourseBase):
    pass


# Actualizar un curso
class CourseUpdate(BaseModel):
    title: str | None = Field(None, min_length=5, max_length=50)
    description: str | None = Field(None, min_length=10, description="Descripciòn del curso")
    is_active: bool | None = Field(None)


# Leer un curso de la bbdd
class CourseOut(CourseBase):
    is_active: bool
    id: int

    model_config = {'from_attributes': True}


# Esquemas para lecciones
class LessonBase(BaseModel):
    title: str = Field(..., min_length=5, max_length=50, description="Titulo de la descripciòn")


class LessonCreate(LessonBase):
    pass


class LessonUpdate(LessonBase):
    pass


class LessonOut(LessonBase):
    id: int

    model_config = {'from_attributes': True}