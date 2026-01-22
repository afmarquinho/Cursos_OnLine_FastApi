from pydantic import BaseModel, Field, field_validator


# Esquemas para cursos

# Base común
# Esquemas para enrollment
class EnrollementBase(BaseModel):
    student_id: int = Field(..., gt=0, description="Id del estudiante")
    course_id: int = Field(..., gt=0, description="Id del curso")

class EnrollmentCreate(EnrollementBase):
    pass

class EnrollmentUpdate(BaseModel):
    student_id: int | None = Field(None, gt=0)
    course_id: int | None = Field(None, gt=0)
    completed: bool | None = Field(None)
    grade: float | None = Field(None, gt=0.00)

    @field_validator("grade")
    def validate_grade(cls, value):
        if value < 0:
            raise ValueError("La nota no puede ser menor de que cero")
        elif value > 10:
            raise ValueError("la nota no puede ser mayor de 10.00")
        return value


class EnrollmentOut(EnrollementBase):
    completed: bool
    grade: float

    model_config = {'from_attributes': True}
