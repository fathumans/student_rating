from app.storage import json_storage

DEFAULT_STUDENTS = [
    {"id": 1, "name": "Иванов Иван Иванович", "group": "БИН-24-1"},
    {"id": 2, "name": "Петров Петр Петрович", "group": "БИН-24-1"},
    {"id": 3, "name": "Сидоров Сидор Сидорович", "group": "БИН-24-1"},
    {"id": 4, "name": "Кузнецов Алексей Викторович", "group": "БИН-24-1"},
    {"id": 5, "name": "Смирнова Анна Павловна", "group": "БИН-24-1"},
]

DEFAULT_SUBJECTS = [
    {"id": 1, "name": "Математика", "type": "exam", "weight": 0.4},
    {"id": 2, "name": "Программирование", "type": "exam", "weight": 0.3},
    {"id": 3, "name": "Физика", "type": "test", "weight": 0.2},
    {"id": 4, "name": "История", "type": "test", "weight": 0.1},
]

DEFAULT_GRADES = [
    # 2024-весна
    {"id": 1, "student_id": 1, "subject_id": 1, "period": "2024-весна", "value": 4},
    {"id": 2, "student_id": 1, "subject_id": 2, "period": "2024-весна", "value": 4},
    {"id": 3, "student_id": 1, "subject_id": 3, "period": "2024-весна", "value": 4},
    {"id": 4, "student_id": 1, "subject_id": 4, "period": "2024-весна", "value": 5},

    {"id": 5, "student_id": 2, "subject_id": 1, "period": "2024-весна", "value": 4},
    {"id": 6, "student_id": 2, "subject_id": 2, "period": "2024-весна", "value": 4},
    {"id": 7, "student_id": 2, "subject_id": 3, "period": "2024-весна", "value": 4},
    {"id": 8, "student_id": 2, "subject_id": 4, "period": "2024-весна", "value": 4},

    {"id": 9, "student_id": 3, "subject_id": 1, "period": "2024-весна", "value": 3},
    {"id": 10, "student_id": 3, "subject_id": 2, "period": "2024-весна", "value": 3},
    {"id": 11, "student_id": 3, "subject_id": 3, "period": "2024-весна", "value": 3},
    {"id": 12, "student_id": 3, "subject_id": 4, "period": "2024-весна", "value": 3},

    {"id": 13, "student_id": 4, "subject_id": 1, "period": "2024-весна", "value": 3},
    {"id": 14, "student_id": 4, "subject_id": 2, "period": "2024-весна", "value": 2},
    {"id": 15, "student_id": 4, "subject_id": 3, "period": "2024-весна", "value": 2},
    {"id": 16, "student_id": 4, "subject_id": 4, "period": "2024-весна", "value": 3},

    {"id": 17, "student_id": 5, "subject_id": 1, "period": "2024-весна", "value": 5},
    {"id": 18, "student_id": 5, "subject_id": 2, "period": "2024-весна", "value": 5},
    {"id": 19, "student_id": 5, "subject_id": 3, "period": "2024-весна", "value": 4},
    {"id": 20, "student_id": 5, "subject_id": 4, "period": "2024-весна", "value": 5},

    # 2024-осень
    {"id": 21, "student_id": 1, "subject_id": 1, "period": "2024-осень", "value": 5},
    {"id": 22, "student_id": 1, "subject_id": 2, "period": "2024-осень", "value": 5},
    {"id": 23, "student_id": 1, "subject_id": 3, "period": "2024-осень", "value": 5},
    {"id": 24, "student_id": 1, "subject_id": 4, "period": "2024-осень", "value": 5},

    {"id": 25, "student_id": 2, "subject_id": 1, "period": "2024-осень", "value": 4},
    {"id": 26, "student_id": 2, "subject_id": 2, "period": "2024-осень", "value": 5},
    {"id": 27, "student_id": 2, "subject_id": 3, "period": "2024-осень", "value": 4},
    {"id": 28, "student_id": 2, "subject_id": 4, "period": "2024-осень", "value": 4},

    {"id": 29, "student_id": 3, "subject_id": 1, "period": "2024-осень", "value": 4},
    {"id": 30, "student_id": 3, "subject_id": 2, "period": "2024-осень", "value": 4},
    {"id": 31, "student_id": 3, "subject_id": 3, "period": "2024-осень", "value": 3},
    {"id": 32, "student_id": 3, "subject_id": 4, "period": "2024-осень", "value": 4},

    {"id": 33, "student_id": 4, "subject_id": 1, "period": "2024-осень", "value": 3},
    {"id": 34, "student_id": 4, "subject_id": 2, "period": "2024-осень", "value": 3},
    {"id": 35, "student_id": 4, "subject_id": 3, "period": "2024-осень", "value": 3},
    {"id": 36, "student_id": 4, "subject_id": 4, "period": "2024-осень", "value": 3},

    {"id": 37, "student_id": 5, "subject_id": 1, "period": "2024-осень", "value": 5},
    {"id": 38, "student_id": 5, "subject_id": 2, "period": "2024-осень", "value": 5},
    {"id": 39, "student_id": 5, "subject_id": 3, "period": "2024-осень", "value": 5},
    {"id": 40, "student_id": 5, "subject_id": 4, "period": "2024-осень", "value": 5},
]


def seed_if_empty():
    """Заполняет файлы дефолтными данными, если они пустые."""
    students = json_storage.load_students()
    if not students:
        json_storage.save_json("students.json", DEFAULT_STUDENTS)

    subjects = json_storage.load_subjects()
    if not subjects:
        json_storage.save_json("subjects.json", DEFAULT_SUBJECTS)

    grades = json_storage.load_grades()
    if not grades:
        json_storage.save_json("grades.json", DEFAULT_GRADES)