from app.core.analyzer import (
    find_problem_subjects,
    find_problem_students,
    get_subject_statistics,
)

SUBJECTS = [
    {"id": 1, "name": "Архитектура ЭВМ", "type": "exam", "weight": 1.0},
    {"id": 2, "name": "ИЯ", "type": "test", "weight": 0.6},
]

STUDENTS = [
    {"id": 1, "name": "Анисимов Н.С."},
    {"id": 2, "name": "Горин Д.В."},
    {"id": 3, "name": "Мельников Ю.Д."},
]


def test_find_problem_subjects():
    # Мельников: 58 (неуд), Горин: 83 (уд), Анисимов: 93 (отл)
    grades = [
        {"student_id": 1, "subject_id": 1, "current": 38, "final": 55},
        {"student_id": 2, "subject_id": 1, "current": 35, "final": 48},
        {"student_id": 3, "subject_id": 1, "current": 28, "final": 30},
    ]
    result = find_problem_subjects(grades, SUBJECTS, threshold=0.20)
    assert len(result) == 1
    assert result[0]["subject_name"] == "Архитектура ЭВМ"
    assert result[0]["bad_rate"] == 0.33  # 1 из 3 < 61
    assert result[0]["average_score"] == 78.0


def test_find_problem_subjects_no_problems():
    grades = [
        {"student_id": 1, "subject_id": 1, "current": 40, "final": 60},
        {"student_id": 2, "subject_id": 1, "current": 40, "final": 60},
    ]
    result = find_problem_subjects(grades, SUBJECTS, threshold=0.20)
    assert len(result) == 0


def test_find_problem_students():
    grades = [
        {"student_id": 1, "subject_id": 1, "current": 40, "final": 60},
        {"student_id": 2, "subject_id": 1, "current": 30, "final": 30},
        {"student_id": 3, "subject_id": 1, "current": 25, "final": 28},
    ]
    result = find_problem_students(STUDENTS, grades, SUBJECTS, threshold=61.0)
    assert len(result) == 2
    # Сортировка по убыванию рейтинга (ниже рейтинг = хуже), но в find_problem_students нет сортировки
    # Проверяем просто наличие
    names = [r["name"] for r in result]
    assert "Мельников Ю.Д." in names
    assert "Горин Д.В." in names


def test_get_subject_statistics():
    grades = [
        {"student_id": 1, "subject_id": 1, "current": 40, "final": 60},
        {"student_id": 2, "subject_id": 1, "current": 30, "final": 30},
        {"student_id": 3, "subject_id": 1, "current": 35, "final": 40},
    ]
    result = get_subject_statistics(grades, SUBJECTS)
    assert len(result) == 1
    assert result[0]["subject_name"] == "Архитектура ЭВМ"
    assert result[0]["average"] == 78.33
    assert result[0]["min"] == 60
    assert result[0]["max"] == 100
    assert result[0]["median"] == 75