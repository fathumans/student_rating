from app.core.ranker import (
    rank_students_absolute,
    rank_students_weighted,
    get_combined_ranking,
)

STUDENTS = [
    {"id": 1, "name": "Анисимов Н.С."},
    {"id": 2, "name": "Горин Д.В."},
    {"id": 3, "name": "Гориченко М.С."},
    {"id": 4, "name": "Жуковец Д.Д."},
    {"id": 5, "name": "Наконечный К.Н."},
]

SUBJECTS = [
    {"id": 1, "name": "Архитектура", "type": "exam", "weight": 1.0},
    {"id": 2, "name": "ИЯ", "type": "test", "weight": 0.6},
    {"id": 3, "name": "ИО", "type": "exam", "weight": 1.0},
]


def test_rank_students_absolute():
    # Анисимов: 97, Гориченко: 100, Жуковец: 70, Наконечный: 84, Горин: 83
    grades = [
        {"student_id": 1, "subject_id": 1, "current": 38, "final": 55},
        {"student_id": 1, "subject_id": 2, "current": 40, "final": 60},
        {"student_id": 1, "subject_id": 3, "current": 40, "final": 58},
        {"student_id": 2, "subject_id": 1, "current": 35, "final": 48},
        {"student_id": 2, "subject_id": 2, "current": 40, "final": 60},
        {"student_id": 2, "subject_id": 3, "current": 36, "final": 45},
        {"student_id": 3, "subject_id": 1, "current": 40, "final": 60},
        {"student_id": 3, "subject_id": 2, "current": 40, "final": 60},
        {"student_id": 3, "subject_id": 3, "current": 40, "final": 60},
        {"student_id": 4, "subject_id": 1, "current": 32, "final": 38},
        {"student_id": 4, "subject_id": 2, "current": 35, "final": 45},
        {"student_id": 4, "subject_id": 3, "current": 33, "final": 40},
        {"student_id": 5, "subject_id": 1, "current": 30, "final": 31},
        {"student_id": 5, "subject_id": 2, "current": 40, "final": 60},
        {"student_id": 5, "subject_id": 3, "current": 40, "final": 51},
    ]
    result = rank_students_absolute(STUDENTS, grades, SUBJECTS)
    assert result[0]["name"] == "Гориченко М.С."
    assert result[0]["absolute_rank"] == 1
    assert result[1]["name"] == "Анисимов Н.С."
    assert result[1]["absolute_rank"] == 2
    assert result[-1]["name"] == "Жуковец Д.Д."
    assert result[-1]["absolute_rank"] == 5


def test_rank_students_weighted():
    # Гориченко: 100, Анисимов: 97.31, Горин: 83.46, Наконечный: 84.62, Жуковец: 70
    grades = [
        {"student_id": 1, "subject_id": 1, "current": 38, "final": 55},
        {"student_id": 1, "subject_id": 2, "current": 40, "final": 60},
        {"student_id": 1, "subject_id": 3, "current": 40, "final": 58},
        {"student_id": 2, "subject_id": 1, "current": 35, "final": 48},
        {"student_id": 2, "subject_id": 2, "current": 40, "final": 60},
        {"student_id": 2, "subject_id": 3, "current": 36, "final": 45},
        {"student_id": 3, "subject_id": 1, "current": 40, "final": 60},
        {"student_id": 3, "subject_id": 2, "current": 40, "final": 60},
        {"student_id": 3, "subject_id": 3, "current": 40, "final": 60},
        {"student_id": 4, "subject_id": 1, "current": 32, "final": 38},
        {"student_id": 4, "subject_id": 2, "current": 35, "final": 45},
        {"student_id": 4, "subject_id": 3, "current": 33, "final": 40},
        {"student_id": 5, "subject_id": 1, "current": 30, "final": 31},
        {"student_id": 5, "subject_id": 2, "current": 40, "final": 60},
        {"student_id": 5, "subject_id": 3, "current": 40, "final": 51},
    ]
    result = rank_students_weighted(STUDENTS, grades, SUBJECTS)
    assert result[0]["name"] == "Гориченко М.С."
    assert result[0]["weighted_rank"] == 1
    assert result[-1]["name"] == "Жуковец Д.Д."


def test_combined_ranking():
    grades = [
        {"student_id": 1, "subject_id": 1, "current": 40, "final": 60},
        {"student_id": 2, "subject_id": 1, "current": 30, "final": 30},
    ]
    subjects = [{"id": 1, "name": "A", "type": "exam", "weight": 1.0}]
    result = get_combined_ranking(STUDENTS[:2], grades, subjects)
    assert len(result) == 2
    assert result[0]["absolute_rating"] == 100.0
    assert result[0]["weighted_rating"] == 100.0
    assert "rating_diff" in result[0]