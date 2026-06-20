from fastapi import APIRouter, HTTPException
from typing import List

from app.storage import json_storage
from app.schemas import SubjectCreate, SubjectOut

router = APIRouter(prefix="/subjects", tags=["Предметы"])


@router.get("", response_model=List[SubjectOut])
def list_subjects():
    return json_storage.load_subjects()


@router.post("", response_model=SubjectOut, status_code=201)
def create_subject(subject: SubjectCreate):
    return json_storage.add_item("subjects.json", subject.model_dump())


@router.get("/{subject_id}", response_model=SubjectOut)
def get_subject(subject_id: int):
    subject = json_storage.get_by_id("subjects.json", subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail="Предмет не найден")
    return subject


@router.put("/{subject_id}", response_model=SubjectOut)
def update_subject(subject_id: int, subject: SubjectCreate):
    updated = json_storage.update_item("subjects.json", subject_id, subject.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="Предмет не найден")
    return updated


@router.delete("/{subject_id}", status_code=204)
def delete_subject(subject_id: int):
    if not json_storage.delete_item("subjects.json", subject_id):
        raise HTTPException(status_code=404, detail="Предмет не найден")
    return None