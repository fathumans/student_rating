import pytest
from app.core.aggregator import calculate_weighted_rating, calculate_group_average

SUBJECTS = [
    {"id": 1, "name": "Математика", "weight": 0.5},
    {"id": 2, "name": "Программирование", "weight": 0.3},
    {"id": 3, "name": "Физика", "weight": 0.2},
]


def test_weighted_rating_basic():
    grades = [
        {"student_id": 1, "subject_id": 1, "value": 5},
        {"student_id": 1, "subject_id": 2, "value": 4},
    ]
    # (5*0.5 + 4*0.3) / 0.8 = 4.625
    assert calculate_weighted_rating(1, grades, SUBJECTS) == 4.62


def test_weighted_rating_all_subjects():
    grades = [
        {"student_id": 1, "subject_id": 1, "value": 5},
        {"student_id": 1, "subject_id": 2, "value": 4},
        {"student_id": 1, "subject_id": 3, "value": 3},
    ]
    # (5*0.5 + 4*0.3 + 3*0.2) / 1.0 = 4.3
    assert calculate_weighted_rating(1, grades, SUBJECTS) == 4.3


def test_weighted_rating_empty():
    assert calculate_weighted_rating(1, [], SUBJECTS) == 0.0


def test_weighted_rating_missing_subject():
    grades = [{"student_id": 1, "subject_id": 99, "value": 5}]
    assert calculate_weighted_rating(1, grades, SUBJECTS) == 0.0


def test_group_average():
    grades = [
        {"student_id": 1, "subject_id": 1, "value": 5},
        {"student_id": 2, "subject_id": 1, "value": 4},
    ]
    assert calculate_group_average(grades, SUBJECTS) == 4.5