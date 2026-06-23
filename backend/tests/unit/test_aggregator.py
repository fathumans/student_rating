import pytest
from app.core.aggregator import (
    calculate_subject_total,
    calculate_absolute_rating,
    calculate_weighted_rating,
    calculate_group_average_absolute,
    calculate_group_average_weighted,
    get_student_subjects_detail,
)

SUBJECTS = [
    {"id": 1, "name": "Архитектура ЭВМ", "type": "exam", "weight": 1.0},
    {"id": 2, "name": "Иностранный язык", "type": "test", "weight": 0.6},
    {"id": 3, "name": "Исследование операций", "type": "exam", "weight": 1.0},
]


def test_calculate_subject_total():
    grade = {"current": 30, "final": 45}
    assert calculate_subject_total(grade) == 75


def test_calculate_subject_total_capped():
    grade = {"current": 40, "final": 70}
    assert calculate_subject_total(grade) == 100


def test_calculate_subject_total_missing_fields():
    grade = {"current": 20}
    assert calculate_subject_total(grade) == 20


def test_calculate_absolute_rating():
    # Анисимов: (93 + 100 + 98) / 3 = 97.0
    grades = [
        {"student_id": 1, "subject_id": 1, "current": 38, "final": 55},
        {"student_id": 1, "subject_id": 2, "current": 40, "final": 60},
        {"student_id": 1, "subject_id": 3, "current": 40, "final": 58},
    ]
    assert calculate_absolute_rating(1, grades, SUBJECTS) == 97.0


def test_calculate_weighted_rating():
    # Анисимов: (93*1.0 + 100*0.6 + 98*1.0) / (1.0 + 0.6 + 1.0) = 251 / 2.6 = 96.54
    grades = [
        {"student_id": 1, "subject_id": 1, "current": 38, "final": 55},
        {"student_id": 1, "subject_id": 2, "current": 40, "final": 60},
        {"student_id": 1, "subject_id": 3, "current": 40, "final": 58},
    ]
    assert calculate_weighted_rating(1, grades, SUBJECTS) == 96.54


def test_calculate_weighted_rating_with_zero_weight_subject():
    # Предмет с весом 0 не влияет
    subjects_with_zero = [
        {"id": 1, "name": "A", "type": "exam", "weight": 1.0},
        {"id": 2, "name": "B", "type": "test", "weight": 0.0},
    ]
    grades = [
        {"student_id": 1, "subject_id": 1, "current": 30, "final": 30},
        {"student_id": 1, "subject_id": 2, "current": 40, "final": 60},
    ]
    assert calculate_weighted_rating(1, grades, subjects_with_zero) == 60.0


def test_calculate_absolute_rating_empty():
    assert calculate_absolute_rating(1, [], SUBJECTS) == 0.0


def test_calculate_group_average_absolute():
    grades = [
        {"student_id": 1, "subject_id": 1, "current": 40, "final": 60},
        {"student_id": 2, "subject_id": 1, "current": 30, "final": 30},
    ]
    assert calculate_group_average_absolute(grades, SUBJECTS) == 80.0


def test_get_student_subjects_detail():
    grades = [
        {"student_id": 1, "subject_id": 1, "current": 30, "final": 31},
        {"student_id": 1, "subject_id": 2, "current": 40, "final": 60},
    ]
    result = get_student_subjects_detail(1, grades, SUBJECTS)
    assert len(result) == 2
    assert result[0]["subject_name"] == "Архитектура ЭВМ"
    assert result[0]["total_score"] == 61
    assert result[0]["grade"] == 3
    assert result[0]["status"] == "Удовлетворительно"
    assert result[1]["total_score"] == 100
    assert result[1]["grade"] == 5