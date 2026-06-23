from fastapi import APIRouter, HTTPException
from typing import List

from app.storage import json_storage
from app.core.converter import convert_student_grades
from app.schemas import GradeCreate, GradeOut

router = APIRouter(prefix="/grades", tags=["Оценки"])


def _enrich_grade(grade: dict) -> dict:
    """Добавляет вычисляемые поля total_score, grade, status."""
    from app.core.converter import score_to_grade, score_to_status
    current = grade.get("current", 0) or 0
    final = grade.get("final", 0) or 0
    total = min(current + final, 100)
    return {
        **grade,
        "total_score": total,
        "grade": score_to_grade(total),
        "status": score_to_status(total),
    }


@router.get("", response_model=List[GradeOut])
def list_grades(student_id: int = None, subject_id: int = None, period: str = None):
    grades = json_storage.load_grades()
    if student_id is not None:
        grades = [g for g in grades if g.get("student_id") == student_id]
    if subject_id is not None:
        grades = [g for g in grades if g.get("subject_id") == subject_id]
    if period is not None:
        grades = [g for g in grades if g.get("period") == period]
    return [_enrich_grade(g) for g in grades]


@router.post("", response_model=GradeOut, status_code=201)
def create_grade(grade: GradeCreate):
    data = grade.model_dump()
    result = json_storage.add_item("grades.json", data)
    return _enrich_grade(result)


@router.delete("/{grade_id}", status_code=204)
def delete_grade(grade_id: int):
    if not json_storage.delete_item("grades.json", grade_id):
        raise HTTPException(status_code=404, detail="Оценка не найдена")
    return None