from fastapi import APIRouter, HTTPException
from typing import List

from app.storage import json_storage
from app.schemas import GradeCreate, GradeOut

router = APIRouter(prefix="/grades", tags=["Оценки"])


@router.get("", response_model=List[GradeOut])
def list_grades(student_id: int = None, subject_id: int = None):
    grades = json_storage.load_grades()
    if student_id is not None:
        grades = [g for g in grades if g.get("student_id") == student_id]
    if subject_id is not None:
        grades = [g for g in grades if g.get("subject_id") == subject_id]
    return grades


@router.post("", response_model=GradeOut, status_code=201)
def create_grade(grade: GradeCreate):
    return json_storage.add_item("grades.json", grade.model_dump())


@router.delete("/{grade_id}", status_code=204)
def delete_grade(grade_id: int):
    if not json_storage.delete_item("grades.json", grade_id):
        raise HTTPException(status_code=404, detail="Оценка не найдена")
    return None