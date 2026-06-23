from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List


# === СТУДЕНТЫ (без изменений) ===
class StudentBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    group: str = Field(default="БИН-24-1", min_length=1, max_length=20)


class StudentCreate(StudentBase):
    pass


class StudentOut(StudentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# === ПРЕДМЕТЫ (без изменений) ===
class SubjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    type: str = Field(default="exam", pattern="^(exam|test|practice)$")
    weight: float = Field(default=1.0, ge=0.0, le=1.0)


class SubjectCreate(SubjectBase):
    pass


class SubjectOut(SubjectBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# === ОЦЕНКИ — НОВАЯ СТРУКТУРА ===
class GradeBase(BaseModel):
    student_id: int = Field(..., gt=0)
    subject_id: int = Field(..., gt=0)
    period: str = Field(..., min_length=1, max_length=50)
    current: int = Field(..., ge=0, le=40, description="Текущая аттестация, 0-40 баллов")
    final: int = Field(..., ge=0, le=60, description="Промежуточная аттестация, 0-60 баллов")


class GradeCreate(GradeBase):
    pass


class GradeOut(GradeBase):
    id: int
    total_score: Optional[int] = Field(default=None, description="Итоговый балл 0-100")
    grade: Optional[int] = Field(default=None, description="Оценка 2-5")
    status: Optional[str] = Field(default=None, description="Текстовый статус")
    model_config = ConfigDict(from_attributes=True)


# === РЕЙТИНГ — НОВЫЕ СХЕМЫ ===
class RatingItem(BaseModel):
    id: int
    name: str
    group: str
    absolute_rating: float = Field(..., description="Средний балл 0-100")
    absolute_rank: int
    weighted_rating: float = Field(..., description="Взвешенный средний балл 0-100")
    weighted_rank: int
    rating_diff: int = Field(..., description="Разница позиций: абс - взвеш")
    excellent_count: int = Field(..., description="Количество предметов 91+")

    model_config = ConfigDict(extra='ignore', from_attributes=True)


class SubjectDetail(BaseModel):
    subject_id: int
    subject_name: str
    type: str
    weight: float
    current: int
    final: int
    total_score: int
    grade: int
    status: str


class StudentDetail(BaseModel):
    student: StudentOut
    subjects: List[SubjectDetail]
    absolute_rating: float
    weighted_rating: float


class ProblemSubject(BaseModel):
    subject_id: int
    subject_name: str
    bad_rate: float
    average_score: float
    min_score: int
    max_score: int
    total_students: int


class PeriodComparison(BaseModel):
    period1: str
    period2: str
    absolute: dict
    weighted: dict


class SubjectStatistics(BaseModel):
    subject_id: int
    subject_name: str
    average: float
    median: float
    std_dev: float
    min: int
    max: int