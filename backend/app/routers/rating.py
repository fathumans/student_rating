from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse
from typing import List

from app.storage import json_storage, csv_exporter
from app.core import aggregator, ranker, analyzer, dynamics
from app.schemas import RatingItem, ProblemSubject, PeriodComparison, StudentDetail, SubjectStatistics

router = APIRouter(prefix="/rating", tags=["Рейтинг"])


@router.get("")  # убрали response_model=List[RatingItem]
def get_rating():
    students = json_storage.load_students()
    grades = json_storage.load_grades()
    subjects = json_storage.load_subjects()
    if not students or not grades:
        return []
    return ranker.get_combined_ranking(students, grades, subjects)


@router.get("/absolute", response_model=List[dict])
def get_absolute_rating():
    students = json_storage.load_students()
    grades = json_storage.load_grades()
    subjects = json_storage.load_subjects()
    return ranker.rank_students_absolute(students, grades, subjects)


@router.get("/weighted", response_model=List[dict])
def get_weighted_rating():
    students = json_storage.load_students()
    grades = json_storage.load_grades()
    subjects = json_storage.load_subjects()
    return ranker.rank_students_weighted(students, grades, subjects)


@router.get("/student/{student_id}", response_model=StudentDetail)
def get_student_detail(student_id: int):
    students = json_storage.load_students()
    grades = json_storage.load_grades()
    subjects = json_storage.load_subjects()

    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")

    return {
        "student": student,
        "subjects": aggregator.get_student_subjects_detail(student_id, grades, subjects),
        "absolute_rating": aggregator.calculate_absolute_rating(student_id, grades, subjects),
        "weighted_rating": aggregator.calculate_weighted_rating(student_id, grades, subjects),
    }


@router.get("/problems", response_model=List[ProblemSubject])
def get_problem_subjects(threshold: float = 0.20):
    grades = json_storage.load_grades()
    subjects = json_storage.load_subjects()
    return analyzer.find_problem_subjects(grades, subjects, threshold)


@router.get("/statistics", response_model=List[SubjectStatistics])
def get_subjects_statistics():
    grades = json_storage.load_grades()
    subjects = json_storage.load_subjects()
    return analyzer.get_subject_statistics(grades, subjects)


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

    ranked = ranker.get_combined_ranking(students, grades, subjects)
    csv_content = csv_exporter.export_rating_to_csv(ranked)

    return PlainTextResponse(
        content=csv_content,
        media_type="text/csv; charset=utf-8-sig",
        headers={"Content-Disposition": "attachment; filename=rating.csv"}
    )