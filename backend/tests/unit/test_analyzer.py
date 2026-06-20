from app.core.analyzer import find_problem_subjects, find_problem_students

SUBJECTS = [
    {"id": 1, "name": "Математика", "weight": 1.0},
    {"id": 2, "name": "Физика", "weight": 1.0},
]

STUDENTS = [
    {"id": 1, "name": "Иванов И.И."},
    {"id": 2, "name": "Петров П.П."},
]


def test_find_problem_subjects():
    grades = [
        {"student_id": 1, "subject_id": 1, "value": 2},
        {"student_id": 2, "subject_id": 1, "value": 2},
        {"student_id": 1, "subject_id": 2, "value": 5},
        {"student_id": 2, "subject_id": 2, "value": 5},
    ]
    result = find_problem_subjects(grades, SUBJECTS, threshold=0.15)
    assert len(result) == 1
    assert result[0]["subject_name"] == "Математика"
    assert result[0]["bad_rate"] == 1.0


def test_find_problem_students():
    grades = [
        {"student_id": 1, "subject_id": 1, "value": 2},
        {"student_id": 2, "subject_id": 1, "value": 5},
    ]
    result = find_problem_students(STUDENTS, grades, SUBJECTS, threshold=2.5)
    assert len(result) == 1
    assert result[0]["name"] == "Иванов И.И."