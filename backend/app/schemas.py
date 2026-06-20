from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List


class StudentBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    group: str = Field(default="БИН-24-1", min_length=1, max_length=20)


class StudentCreate(StudentBase):
    pass


class StudentOut(StudentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SubjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    type: str = Field(default="exam", pattern="^(exam|test|practice)$")
    weight: float = Field(default=1.0, ge=0.0, le=1.0)


class SubjectCreate(SubjectBase):
    pass


class SubjectOut(SubjectBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class GradeBase(BaseModel):
    student_id: int = Field(..., gt=0)
    subject_id: int = Field(..., gt=0)
    period: str = Field(..., min_length=1, max_length=50)
    value: int = Field(..., ge=2, le=5)


class GradeCreate(GradeBase):
    pass


class GradeOut(GradeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class RatingItem(BaseModel):
    id: int
    name: str
    group: str
    rating: float
    fives_count: int
    rank: int


class ProblemSubject(BaseModel):
    subject_id: int
    subject_name: str
    bad_rate: float
    average: float
    total_students: int


class PeriodComparison(BaseModel):
    period1: str
    period2: str
    average1: float
    average2: float
    delta: float
    trend: str