from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse
from typing import List

from app.storage import json_storage, csv_exporter
from app.core import aggregator, ranker, analyzer, dynamics
from app.schemas import RatingItem, ProblemSubject, PeriodComparison

router = APIRouter(prefix="/rating", tags=["Рейтинг"])


@router.get("", response_model=List[RatingItem])
def get_rating():
    students = json_storage.load_students()
    grades = json_storage.load_grades()
    subjects = json_storage.load_subjects()
    if not students or not grades:
        return []
    return ranker.rank_students(students, grades, subjects)


@router.get("/problems", response_model=List[ProblemSubject])
def get_problem_subjects(threshold: float = 0.15):
    grades = json_storage.load_grades()
    subjects = json_storage.load_subjects()
    return analyzer.find_problem_subjects(grades, subjects, threshold)


@router.get("/dynamics")
def get_dynamics(period1: str, period2: str):
    grades = json_storage.load_grades()
    subjects = json_storage.load_subjects()
    if not grades:
        raise HTTPException(status_code=400, detail="Нет данных об оценках")
    return dynamics.compare_periods(grades, subjects, period1, period2)


@router.get("/export", response_class=PlainTextResponse)
def export_csv():
    students = json_storage.load_students()
    grades = json_storage.load_grades()
    subjects = json_storage.load_subjects()
    if not students or not grades:
        raise HTTPException(status_code=400, detail="Нет данных для экспорта")

    ranked = ranker.rank_students(students, grades, subjects)
    csv_content = csv_exporter.export_rating_to_csv(ranked)

    return PlainTextResponse(
        content=csv_content,
        media_type="text/csv; charset=utf-8-sig",
        headers={"Content-Disposition": "attachment; filename=rating.csv"}
    )