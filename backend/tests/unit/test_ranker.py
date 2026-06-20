from app.core.ranker import rank_students

STUDENTS = [
    {"id": 1, "name": "Иванов И.И."},
    {"id": 2, "name": "Петров П.П."},
    {"id": 3, "name": "Сидоров С.С."},
]

SUBJECTS = [
    {"id": 1, "name": "Математика", "weight": 0.5},
    {"id": 2, "name": "Физика", "weight": 0.5},
]


def test_rank_by_rating_desc():
    grades = [
        {"student_id": 1, "subject_id": 1, "value": 5},
        {"student_id": 1, "subject_id": 2, "value": 5},
        {"student_id": 2, "subject_id": 1, "value": 4},
        {"student_id": 2, "subject_id": 2, "value": 4},
        {"student_id": 3, "subject_id": 1, "value": 3},
        {"student_id": 3, "subject_id": 2, "value": 3},
    ]
    result = rank_students(STUDENTS, grades, SUBJECTS)
    assert result[0]["rank"] == 1 and result[0]["name"] == "Иванов И.И."
    assert result[1]["rank"] == 2 and result[1]["name"] == "Петров П.П."
    assert result[2]["rank"] == 3 and result[2]["name"] == "Сидоров С.С."


def test_rank_tie_by_fives_and_name():
    # Одинаковый рейтинг 4.5, одинаковое число пятёрок (1) -> алфавит
    grades = [
        {"student_id": 1, "subject_id": 1, "value": 5},
        {"student_id": 1, "subject_id": 2, "value": 4},
        {"student_id": 2, "subject_id": 1, "value": 4},
        {"student_id": 2, "subject_id": 2, "value": 5},
    ]
    result = rank_students(STUDENTS[:2], grades, SUBJECTS)
    assert result[0]["name"] == "Иванов И.И."  # раньше по алфавиту
    assert result[1]["name"] == "Петров П.П."