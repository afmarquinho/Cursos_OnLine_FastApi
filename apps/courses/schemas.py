from pydantic import BaseModel, Field, field_validator

# -------------------------
# Esquemas para cursos
# -------------------------

class CourseBase(BaseModel):
    title: str = Field(..., min_length=5, max_length=50, description="Nombre del curso")
    description: str = Field(..., min_length=10, description="Descripción del curso")

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    title: str | None = Field(None, min_length=5, max_length=50)
    description: str | None = Field(None, min_length=10, description="Descripción del curso")
    is_active: bool | None = Field(None)

class CourseOut(CourseBase):
    is_active: bool
    id: int

    model_config = {'from_attributes': True}

# -------------------------
# Esquemas para lecciones
# -------------------------

class LessonBase(BaseModel):
    title: str = Field(..., min_length=5, max_length=50, description="Título de la lección")
    professor_id: int

    @field_validator("professor_id")
    def is_positive(cls, value):
        if value < 1:
            raise ValueError("Id del profesor incorrecto")
        return value

class LessonCreate(LessonBase):
    pass

class LessonUpdate(BaseModel):
    title: str | None = Field(None, min_length=5, max_length=50)
    professor_id: int | None = Field(None)

    @field_validator("professor_id")
    def is_positive(cls, value):
        if value is not None and value < 1:
            raise ValueError("Id del profesor incorrecto")
        return value

class LessonOut(LessonBase):
    id: int

    model_config = {'from_attributes': True}

