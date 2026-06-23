import pytest
from app.core.converter import (
    score_to_grade,
    score_to_status,
    score_to_color,
    convert_student_grades,
)


def test_score_to_grade_excellent():
    assert score_to_grade(100) == 5
    assert score_to_grade(91) == 5
    assert score_to_grade(95) == 5


def test_score_to_grade_good():
    assert score_to_grade(90) == 4
    assert score_to_grade(76) == 4
    assert score_to_grade(85) == 4


def test_score_to_grade_satisfactory():
    assert score_to_grade(75) == 3
    assert score_to_grade(61) == 3
    assert score_to_grade(70) == 3


def test_score_to_grade_unsatisfactory():
    assert score_to_grade(60) == 2
    assert score_to_grade(45) == 2
    assert score_to_grade(0) == 2


def test_score_to_status():
    assert score_to_status(95) == "Отлично"
    assert score_to_status(80) == "Хорошо"
    assert score_to_status(65) == "Удовлетворительно"
    assert score_to_status(50) == "Неудовлетворительно"


def test_score_to_color():
    assert score_to_color(95) == "#16a34a"
    assert score_to_color(80) == "#2563eb"
    assert score_to_color(65) == "#ca8a04"
    assert score_to_color(50) == "#dc2626"


def test_convert_student_grades():
    grades = [
        {"student_id": 1, "subject_id": 1, "current": 30, "final": 31},
        {"student_id": 1, "subject_id": 2, "current": 40, "final": 60},
    ]
    result = convert_student_grades(grades)
    assert len(result) == 2
    assert result[0]["total_score"] == 61
    assert result[0]["grade"] == 3
    assert result[0]["status"] == "Удовлетворительно"
    assert result[1]["total_score"] == 100
    assert result[1]["grade"] == 5
    assert result[1]["status"] == "Отлично"


def test_convert_student_grades_capped_at_100():
    grades = [{"student_id": 1, "subject_id": 1, "current": 40, "final": 70}]
    result = convert_student_grades(grades)
    assert result[0]["total_score"] == 100