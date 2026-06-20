from fastapi import APIRouter, HTTPException
from typing import List

from app.storage import json_storage
from app.schemas import StudentCreate, StudentOut

router = APIRouter(prefix="/students", tags=["Студенты"])


@router.get("", response_model=List[StudentOut])
def list_students():
    return json_storage.load_students()


@router.post("", response_model=StudentOut, status_code=201)
def create_student(student: StudentCreate):
    data = student.model_dump()
    return json_storage.add_item("students.json", data)


@router.get("/{student_id}", response_model=StudentOut)
def get_student(student_id: int):
    student = json_storage.get_by_id("students.json", student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")
    return student


@router.put("/{student_id}", response_model=StudentOut)
def update_student(student_id: int, student: StudentCreate):
    updated = json_storage.update_item("students.json", student_id, student.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="Студент не найден")
    return updated


@router.delete("/{student_id}", status_code=204)
def delete_student(student_id: int):
    if not json_storage.delete_item("students.json", student_id):
        raise HTTPException(status_code=404, detail="Студент не найден")
    return None