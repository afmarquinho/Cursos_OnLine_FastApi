from pydantic import BaseModel, Field, field_validator


# Esquemas para cursos

# Base común
0
# Esquemas para enrollment
class EnrollementBase(BaseModel):
    student_id: int = Field(..., gt=0, description="Id del estudiante")
    course_id: int = Field(..., gt=0, description="Id del curso")

    @field_validator("grade")
    def equal_greater_than_zero(cls, value):
        if value < 0:
            raise ValueError("La nota no puede ser menor de que cero")
        elif value > 10:
            raise ValueError("la nota no puede ser mayor de 10.00")
        return value


class EnrollmentCreate(EnrollementBase):
    pass


class EnrollmentUpdate(BaseModel):
    student_id: int | None = Field(None, gt=0)
    course_id: int | None = Field(None, gt=0)
    completed: bool | None = Field(None)
    grade: float | None = Field(None, gt=0.00)


class EnrollmentOut(EnrollementBase):
    completed: bool
    grade: float
    id: int

    model_config = {'from_attributes': True}
