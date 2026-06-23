from app.storage import json_storage

DEFAULT_STUDENTS = [
    {"id": 1, "name": "Анисимов Никита Сергеевич", "group": "БИН-24-1"},
    {"id": 2, "name": "Горин Даниил Витальевич", "group": "БИН-24-1"},
    {"id": 3, "name": "Гориченко Максим Сергеевич", "group": "БИН-24-1"},
    {"id": 4, "name": "Жуковец Даниил Денисович", "group": "БИН-24-1"},
    {"id": 5, "name": "Конопельный Родион Сергеевич", "group": "БИН-24-1"},
    {"id": 6, "name": "Косенков Михаил Алексеевич", "group": "БИН-24-1"},
    {"id": 7, "name": "Медведев Даниил Владимирович", "group": "БИН-24-1"},
    {"id": 8, "name": "Мельников Юрий Денисович", "group": "БИН-24-1"},
    {"id": 9, "name": "Наконечный Кирилл Николаевич", "group": "БИН-24-1"},
    {"id": 10, "name": "Овсянников Илья Андреевич", "group": "БИН-24-1"},
    {"id": 11, "name": "Пшенко Алёна Александровна", "group": "БИН-24-1"},
    {"id": 12, "name": "Сергеев Сергей Владимирович", "group": "БИН-24-1"},
    {"id": 13, "name": "Слесарчук Дмитрий Тимофеевич", "group": "БИН-24-1"},
    {"id": 14, "name": "Терещенко Платон Андреевич", "group": "БИН-24-1"},
    {"id": 15, "name": "Фоменко Егор Евгеньевич", "group": "БИН-24-1"},
    {"id": 16, "name": "Холодилин Константин Сергеевич", "group": "БИН-24-1"},
]

DEFAULT_SUBJECTS = [
    {"id": 1, "name": "Архитектура ЭВМ", "type": "exam", "weight": 0.12},
    {"id": 2, "name": "Иностранный язык в сфере ИТ", "type": "test", "weight": 0.08},
    {"id": 3, "name": "Исследование операций", "type": "exam", "weight": 0.12},
    {"id": 4, "name": "Операционные системы", "type": "exam", "weight": 0.12},
    {"id": 5, "name": "Прикладная физическая культура", "type": "test", "weight": 0.06},
    {"id": 6, "name": "Программирование на Java", "type": "exam", "weight": 0.15},
    {"id": 7, "name": "Проектная деятельность", "type": "test", "weight": 0.10},
    {"id": 8, "name": "Теория вероятностей и мат. статистика", "type": "exam", "weight": 0.12},
    {"id": 9, "name": "Технология облачных вычислений", "type": "test", "weight": 0.08},
    {"id": 10, "name": "Учебная ознакомительная практика", "type": "practice", "weight": 0.05},
]

# 2024-весна — реалистичные оценки
# Профили: отличник (5), хорошист (4), средний (3-4), троечник (3)
DEFAULT_GRADES_2024_VESNA = [
    # === Анисимов (1) — отличник ===
    {"id": 1, "student_id": 1, "subject_id": 1, "period": "2024-весна", "value": 5},
    {"id": 2, "student_id": 1, "subject_id": 2, "period": "2024-весна", "value": 5},
    {"id": 3, "student_id": 1, "subject_id": 3, "period": "2024-весна", "value": 5},
    {"id": 4, "student_id": 1, "subject_id": 4, "period": "2024-весна", "value": 5},
    {"id": 5, "student_id": 1, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 6, "student_id": 1, "subject_id": 6, "period": "2024-весна", "value": 5},
    {"id": 7, "student_id": 1, "subject_id": 7, "period": "2024-весна", "value": 5},
    {"id": 8, "student_id": 1, "subject_id": 8, "period": "2024-весна", "value": 5},
    {"id": 9, "student_id": 1, "subject_id": 9, "period": "2024-весна", "value": 5},
    {"id": 10, "student_id": 1, "subject_id": 10, "period": "2024-весна", "value": 5},

    # === Горин (2) — хорошист ===
    {"id": 11, "student_id": 2, "subject_id": 1, "period": "2024-весна", "value": 4},
    {"id": 12, "student_id": 2, "subject_id": 2, "period": "2024-весна", "value": 5},
    {"id": 13, "student_id": 2, "subject_id": 3, "period": "2024-весна", "value": 4},
    {"id": 14, "student_id": 2, "subject_id": 4, "period": "2024-весна", "value": 4},
    {"id": 15, "student_id": 2, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 16, "student_id": 2, "subject_id": 6, "period": "2024-весна", "value": 4},
    {"id": 17, "student_id": 2, "subject_id": 7, "period": "2024-весна", "value": 4},
    {"id": 18, "student_id": 2, "subject_id": 8, "period": "2024-весна", "value": 4},
    {"id": 19, "student_id": 2, "subject_id": 9, "period": "2024-весна", "value": 5},
    {"id": 20, "student_id": 2, "subject_id": 10, "period": "2024-весна", "value": 4},

    # === Гориченко (3) — отличник ===
    {"id": 21, "student_id": 3, "subject_id": 1, "period": "2024-весна", "value": 5},
    {"id": 22, "student_id": 3, "subject_id": 2, "period": "2024-весна", "value": 5},
    {"id": 23, "student_id": 3, "subject_id": 3, "period": "2024-весна", "value": 5},
    {"id": 24, "student_id": 3, "subject_id": 4, "period": "2024-весна", "value": 5},
    {"id": 25, "student_id": 3, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 26, "student_id": 3, "subject_id": 6, "period": "2024-весна", "value": 5},
    {"id": 27, "student_id": 3, "subject_id": 7, "period": "2024-весна", "value": 5},
    {"id": 28, "student_id": 3, "subject_id": 8, "period": "2024-весна", "value": 5},
    {"id": 29, "student_id": 3, "subject_id": 9, "period": "2024-весна", "value": 5},
    {"id": 30, "student_id": 3, "subject_id": 10, "period": "2024-весна", "value": 5},

    # === Жуковец (4) — средний ===
    {"id": 31, "student_id": 4, "subject_id": 1, "period": "2024-весна", "value": 4},
    {"id": 32, "student_id": 4, "subject_id": 2, "period": "2024-весна", "value": 4},
    {"id": 33, "student_id": 4, "subject_id": 3, "period": "2024-весна", "value": 4},
    {"id": 34, "student_id": 4, "subject_id": 4, "period": "2024-весна", "value": 4},
    {"id": 35, "student_id": 4, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 36, "student_id": 4, "subject_id": 6, "period": "2024-весна", "value": 3},
    {"id": 37, "student_id": 4, "subject_id": 7, "period": "2024-весна", "value": 4},
    {"id": 38, "student_id": 4, "subject_id": 8, "period": "2024-весна", "value": 4},
    {"id": 39, "student_id": 4, "subject_id": 9, "period": "2024-весна", "value": 4},
    {"id": 40, "student_id": 4, "subject_id": 10, "period": "2024-весна", "value": 4},

    # === Конопельный (5) — хорошист ===
    {"id": 41, "student_id": 5, "subject_id": 1, "period": "2024-весна", "value": 4},
    {"id": 42, "student_id": 5, "subject_id": 2, "period": "2024-весна", "value": 5},
    {"id": 43, "student_id": 5, "subject_id": 3, "period": "2024-весна", "value": 4},
    {"id": 44, "student_id": 5, "subject_id": 4, "period": "2024-весна", "value": 5},
    {"id": 45, "student_id": 5, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 46, "student_id": 5, "subject_id": 6, "period": "2024-весна", "value": 4},
    {"id": 47, "student_id": 5, "subject_id": 7, "period": "2024-весна", "value": 5},
    {"id": 48, "student_id": 5, "subject_id": 8, "period": "2024-весна", "value": 4},
    {"id": 49, "student_id": 5, "subject_id": 9, "period": "2024-весна", "value": 5},
    {"id": 50, "student_id": 5, "subject_id": 10, "period": "2024-весна", "value": 4},

    # === Косенков (6) — отличник ===
    {"id": 51, "student_id": 6, "subject_id": 1, "period": "2024-весна", "value": 5},
    {"id": 52, "student_id": 6, "subject_id": 2, "period": "2024-весна", "value": 5},
    {"id": 53, "student_id": 6, "subject_id": 3, "period": "2024-весна", "value": 5},
    {"id": 54, "student_id": 6, "subject_id": 4, "period": "2024-весна", "value": 5},
    {"id": 55, "student_id": 6, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 56, "student_id": 6, "subject_id": 6, "period": "2024-весна", "value": 5},
    {"id": 57, "student_id": 6, "subject_id": 7, "period": "2024-весна", "value": 5},
    {"id": 58, "student_id": 6, "subject_id": 8, "period": "2024-весна", "value": 5},
    {"id": 59, "student_id": 6, "subject_id": 9, "period": "2024-весна", "value": 5},
    {"id": 60, "student_id": 6, "subject_id": 10, "period": "2024-весна", "value": 5},

    # === Медведев (7) — средний ===
    {"id": 61, "student_id": 7, "subject_id": 1, "period": "2024-весна", "value": 4},
    {"id": 62, "student_id": 7, "subject_id": 2, "period": "2024-весна", "value": 4},
    {"id": 63, "student_id": 7, "subject_id": 3, "period": "2024-весна", "value": 3},
    {"id": 64, "student_id": 7, "subject_id": 4, "period": "2024-весна", "value": 4},
    {"id": 65, "student_id": 7, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 66, "student_id": 7, "subject_id": 6, "period": "2024-весна", "value": 4},
    {"id": 67, "student_id": 7, "subject_id": 7, "period": "2024-весна", "value": 3},
    {"id": 68, "student_id": 7, "subject_id": 8, "period": "2024-весна", "value": 4},
    {"id": 69, "student_id": 7, "subject_id": 9, "period": "2024-весна", "value": 4},
    {"id": 70, "student_id": 7, "subject_id": 10, "period": "2024-весна", "value": 4},

    # === Мельников (8) — троечник ===
    {"id": 71, "student_id": 8, "subject_id": 1, "period": "2024-весна", "value": 3},
    {"id": 72, "student_id": 8, "subject_id": 2, "period": "2024-весна", "value": 4},
    {"id": 73, "student_id": 8, "subject_id": 3, "period": "2024-весна", "value": 3},
    {"id": 74, "student_id": 8, "subject_id": 4, "period": "2024-весна", "value": 3},
    {"id": 75, "student_id": 8, "subject_id": 5, "period": "2024-весна", "value": 4},
    {"id": 76, "student_id": 8, "subject_id": 6, "period": "2024-весна", "value": 3},
    {"id": 77, "student_id": 8, "subject_id": 7, "period": "2024-весна", "value": 3},
    {"id": 78, "student_id": 8, "subject_id": 8, "period": "2024-весна", "value": 3},
    {"id": 79, "student_id": 8, "subject_id": 9, "period": "2024-весна", "value": 4},
    {"id": 80, "student_id": 8, "subject_id": 10, "period": "2024-весна", "value": 3},

    # === Наконечный (9) — реальные оценки ===
    {"id": 81, "student_id": 9, "subject_id": 1, "period": "2024-весна", "value": 3},
    {"id": 82, "student_id": 9, "subject_id": 2, "period": "2024-весна", "value": 5},
    {"id": 83, "student_id": 9, "subject_id": 3, "period": "2024-весна", "value": 5},
    {"id": 84, "student_id": 9, "subject_id": 4, "period": "2024-весна", "value": 5},
    {"id": 85, "student_id": 9, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 86, "student_id": 9, "subject_id": 6, "period": "2024-весна", "value": 4},
    {"id": 87, "student_id": 9, "subject_id": 7, "period": "2024-весна", "value": 5},
    {"id": 88, "student_id": 9, "subject_id": 8, "period": "2024-весна", "value": 5},
    {"id": 89, "student_id": 9, "subject_id": 9, "period": "2024-весна", "value": 5},
    {"id": 90, "student_id": 9, "subject_id": 10, "period": "2024-весна", "value": 5},

    # === Овсянников (10) — хорошист ===
    {"id": 91, "student_id": 10, "subject_id": 1, "period": "2024-весна", "value": 4},
    {"id": 92, "student_id": 10, "subject_id": 2, "period": "2024-весна", "value": 5},
    {"id": 93, "student_id": 10, "subject_id": 3, "period": "2024-весна", "value": 4},
    {"id": 94, "student_id": 10, "subject_id": 4, "period": "2024-весна", "value": 4},
    {"id": 95, "student_id": 10, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 96, "student_id": 10, "subject_id": 6, "period": "2024-весна", "value": 4},
    {"id": 97, "student_id": 10, "subject_id": 7, "period": "2024-весна", "value": 4},
    {"id": 98, "student_id": 10, "subject_id": 8, "period": "2024-весна", "value": 4},
    {"id": 99, "student_id": 10, "subject_id": 9, "period": "2024-весна", "value": 5},
    {"id": 100, "student_id": 10, "subject_id": 10, "period": "2024-весна", "value": 4},

    # === Пшенко (11) — отличница ===
    {"id": 101, "student_id": 11, "subject_id": 1, "period": "2024-весна", "value": 5},
    {"id": 102, "student_id": 11, "subject_id": 2, "period": "2024-весна", "value": 5},
    {"id": 103, "student_id": 11, "subject_id": 3, "period": "2024-весна", "value": 5},
    {"id": 104, "student_id": 11, "subject_id": 4, "period": "2024-весна", "value": 5},
    {"id": 105, "student_id": 11, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 106, "student_id": 11, "subject_id": 6, "period": "2024-весна", "value": 5},
    {"id": 107, "student_id": 11, "subject_id": 7, "period": "2024-весна", "value": 5},
    {"id": 108, "student_id": 11, "subject_id": 8, "period": "2024-весна", "value": 5},
    {"id": 109, "student_id": 11, "subject_id": 9, "period": "2024-весна", "value": 5},
    {"id": 110, "student_id": 11, "subject_id": 10, "period": "2024-весна", "value": 5},

    # === Сергеев (12) — средний ===
    {"id": 111, "student_id": 12, "subject_id": 1, "period": "2024-весна", "value": 4},
    {"id": 112, "student_id": 12, "subject_id": 2, "period": "2024-весна", "value": 4},
    {"id": 113, "student_id": 12, "subject_id": 3, "period": "2024-весна", "value": 4},
    {"id": 114, "student_id": 12, "subject_id": 4, "period": "2024-весна", "value": 3},
    {"id": 115, "student_id": 12, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 116, "student_id": 12, "subject_id": 6, "period": "2024-весна", "value": 4},
    {"id": 117, "student_id": 12, "subject_id": 7, "period": "2024-весна", "value": 4},
    {"id": 118, "student_id": 12, "subject_id": 8, "period": "2024-весна", "value": 4},
    {"id": 119, "student_id": 12, "subject_id": 9, "period": "2024-весна", "value": 4},
    {"id": 120, "student_id": 12, "subject_id": 10, "period": "2024-весна", "value": 4},

    # === Слесарчук (13) — хорошист ===
    {"id": 121, "student_id": 13, "subject_id": 1, "period": "2024-весна", "value": 4},
    {"id": 122, "student_id": 13, "subject_id": 2, "period": "2024-весна", "value": 5},
    {"id": 123, "student_id": 13, "subject_id": 3, "period": "2024-весна", "value": 4},
    {"id": 124, "student_id": 13, "subject_id": 4, "period": "2024-весна", "value": 4},
    {"id": 125, "student_id": 13, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 126, "student_id": 13, "subject_id": 6, "period": "2024-весна", "value": 4},
    {"id": 127, "student_id": 13, "subject_id": 7, "period": "2024-весна", "value": 4},
    {"id": 128, "student_id": 13, "subject_id": 8, "period": "2024-весна", "value": 5},
    {"id": 129, "student_id": 13, "subject_id": 9, "period": "2024-весна", "value": 5},
    {"id": 130, "student_id": 13, "subject_id": 10, "period": "2024-весна", "value": 4},

    # === Терещенко (14) — отличник ===
    {"id": 131, "student_id": 14, "subject_id": 1, "period": "2024-весна", "value": 5},
    {"id": 132, "student_id": 14, "subject_id": 2, "period": "2024-весна", "value": 5},
    {"id": 133, "student_id": 14, "subject_id": 3, "period": "2024-весна", "value": 5},
    {"id": 134, "student_id": 14, "subject_id": 4, "period": "2024-весна", "value": 5},
    {"id": 135, "student_id": 14, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 136, "student_id": 14, "subject_id": 6, "period": "2024-весна", "value": 5},
    {"id": 137, "student_id": 14, "subject_id": 7, "period": "2024-весна", "value": 5},
    {"id": 138, "student_id": 14, "subject_id": 8, "period": "2024-весна", "value": 5},
    {"id": 139, "student_id": 14, "subject_id": 9, "period": "2024-весна", "value": 5},
    {"id": 140, "student_id": 14, "subject_id": 10, "period": "2024-весна", "value": 5},

    # === Фоменко (15) — средний ===
    {"id": 141, "student_id": 15, "subject_id": 1, "period": "2024-весна", "value": 4},
    {"id": 142, "student_id": 15, "subject_id": 2, "period": "2024-весна", "value": 4},
    {"id": 143, "student_id": 15, "subject_id": 3, "period": "2024-весна", "value": 4},
    {"id": 144, "student_id": 15, "subject_id": 4, "period": "2024-весна", "value": 4},
    {"id": 145, "student_id": 15, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 146, "student_id": 15, "subject_id": 6, "period": "2024-весна", "value": 3},
    {"id": 147, "student_id": 15, "subject_id": 7, "period": "2024-весна", "value": 4},
    {"id": 148, "student_id": 15, "subject_id": 8, "period": "2024-весна", "value": 4},
    {"id": 149, "student_id": 15, "subject_id": 9, "period": "2024-весна", "value": 4},
    {"id": 150, "student_id": 15, "subject_id": 10, "period": "2024-весна", "value": 4},

    # === Холодилин (16) — хорошист ===
    {"id": 151, "student_id": 16, "subject_id": 1, "period": "2024-весна", "value": 4},
    {"id": 152, "student_id": 16, "subject_id": 2, "period": "2024-весна", "value": 5},
    {"id": 153, "student_id": 16, "subject_id": 3, "period": "2024-весна", "value": 4},
    {"id": 154, "student_id": 16, "subject_id": 4, "period": "2024-весна", "value": 4},
    {"id": 155, "student_id": 16, "subject_id": 5, "period": "2024-весна", "value": 5},
    {"id": 156, "student_id": 16, "subject_id": 6, "period": "2024-весна", "value": 4},
    {"id": 157, "student_id": 16, "subject_id": 7, "period": "2024-весна", "value": 4},
    {"id": 158, "student_id": 16, "subject_id": 8, "period": "2024-весна", "value": 4},
    {"id": 159, "student_id": 16, "subject_id": 9, "period": "2024-весна", "value": 5},
    {"id": 160, "student_id": 16, "subject_id": 10, "period": "2024-весна", "value": 4},
]

# 2023-осень — для динамики (все на балл ниже)
DEFAULT_GRADES_2023_OSEN = [
    # Наконечный (9)
    {"id": 201, "student_id": 9, "subject_id": 1, "period": "2023-осень", "value": 4},
    {"id": 202, "student_id": 9, "subject_id": 2, "period": "2023-осень", "value": 5},
    {"id": 203, "student_id": 9, "subject_id": 3, "period": "2023-осень", "value": 4},
    {"id": 204, "student_id": 9, "subject_id": 4, "period": "2023-осень", "value": 4},
    {"id": 205, "student_id": 9, "subject_id": 5, "period": "2023-осень", "value": 5},
    {"id": 206, "student_id": 9, "subject_id": 6, "period": "2023-осень", "value": 3},
    {"id": 207, "student_id": 9, "subject_id": 7, "period": "2023-осень", "value": 4},
    {"id": 208, "student_id": 9, "subject_id": 8, "period": "2023-осень", "value": 4},
    {"id": 209, "student_id": 9, "subject_id": 9, "period": "2023-осень", "value": 5},
    {"id": 210, "student_id": 9, "subject_id": 10, "period": "2023-осень", "value": 4},

    # Мельников (8) — троечник
    {"id": 211, "student_id": 8, "subject_id": 1, "period": "2023-осень", "value": 3},
    {"id": 212, "student_id": 8, "subject_id": 2, "period": "2023-осень", "value": 3},
    {"id": 213, "student_id": 8, "subject_id": 3, "period": "2023-осень", "value": 3},
    {"id": 214, "student_id": 8, "subject_id": 4, "period": "2023-осень", "value": 3},
    {"id": 215, "student_id": 8, "subject_id": 5, "period": "2023-осень", "value": 4},
    {"id": 216, "student_id": 8, "subject_id": 6, "period": "2023-осень", "value": 3},
    {"id": 217, "student_id": 8, "subject_id": 7, "period": "2023-осень", "value": 3},
    {"id": 218, "student_id": 8, "subject_id": 8, "period": "2023-осень", "value": 3},
    {"id": 219, "student_id": 8, "subject_id": 9, "period": "2023-осень", "value": 3},
    {"id": 220, "student_id": 8, "subject_id": 10, "period": "2023-осень", "value": 3},

    # Анисимов (1) — отличник
    {"id": 221, "student_id": 1, "subject_id": 1, "period": "2023-осень", "value": 5},
    {"id": 222, "student_id": 1, "subject_id": 2, "period": "2023-осень", "value": 5},
    {"id": 223, "student_id": 1, "subject_id": 3, "period": "2023-осень", "value": 5},
    {"id": 224, "student_id": 1, "subject_id": 4, "period": "2023-осень", "value": 5},
    {"id": 225, "student_id": 1, "subject_id": 5, "period": "2023-осень", "value": 5},
    {"id": 226, "student_id": 1, "subject_id": 6, "period": "2023-осень", "value": 5},
    {"id": 227, "student_id": 1, "subject_id": 7, "period": "2023-осень", "value": 5},
    {"id": 228, "student_id": 1, "subject_id": 8, "period": "2023-осень", "value": 5},
    {"id": 229, "student_id": 1, "subject_id": 9, "period": "2023-осень", "value": 5},
    {"id": 230, "student_id": 1, "subject_id": 10, "period": "2023-осень", "value": 5},
]

DEFAULT_GRADES = DEFAULT_GRADES_2024_VESNA + DEFAULT_GRADES_2023_OSEN


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