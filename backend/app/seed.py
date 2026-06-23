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
    {"id": 1, "name": "Архитектура ЭВМ", "type": "exam", "weight": 1.0},
    {"id": 2, "name": "Иностранный язык в сфере ИТ", "type": "test", "weight": 0.6},
    {"id": 3, "name": "Исследование операций", "type": "exam", "weight": 1.0},
    {"id": 4, "name": "Операционные системы", "type": "exam", "weight": 1.0},
    {"id": 5, "name": "Прикладная физическая культура", "type": "test", "weight": 0.6},
    {"id": 6, "name": "Программирование на Java", "type": "exam", "weight": 1.0},
    {"id": 7, "name": "Проектная деятельность", "type": "test", "weight": 0.6},
    {"id": 8, "name": "Теория вероятностей и мат. статистика", "type": "exam", "weight": 1.0},
    {"id": 9, "name": "Технология облачных вычислений", "type": "test", "weight": 0.6},
    {"id": 10, "name": "Учебная ознакомительная практика", "type": "practice", "weight": 1.0},
]

# ==================== 2024-ВЕСНА ====================

# === Анисимов (1) — отличник ===
GRADES_1 = [
    {"id": 1, "student_id": 1, "subject_id": 1, "period": "2024-весна", "current": 38, "final": 55},
    {"id": 2, "student_id": 1, "subject_id": 2, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 3, "student_id": 1, "subject_id": 3, "period": "2024-весна", "current": 40, "final": 58},
    {"id": 4, "student_id": 1, "subject_id": 4, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 5, "student_id": 1, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 50},
    {"id": 6, "student_id": 1, "subject_id": 6, "period": "2024-весна", "current": 40, "final": 58},
    {"id": 7, "student_id": 1, "subject_id": 7, "period": "2024-весна", "current": 40, "final": 55},
    {"id": 8, "student_id": 1, "subject_id": 8, "period": "2024-весна", "current": 40, "final": 56},
    {"id": 9, "student_id": 1, "subject_id": 9, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 10, "student_id": 1, "subject_id": 10, "period": "2024-весна", "current": 40, "final": 60},
]

# === Горин (2) — хорошист ===
GRADES_2 = [
    {"id": 11, "student_id": 2, "subject_id": 1, "period": "2024-весна", "current": 35, "final": 48},
    {"id": 12, "student_id": 2, "subject_id": 2, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 13, "student_id": 2, "subject_id": 3, "period": "2024-весна", "current": 36, "final": 45},
    {"id": 14, "student_id": 2, "subject_id": 4, "period": "2024-весна", "current": 35, "final": 50},
    {"id": 15, "student_id": 2, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 50},
    {"id": 16, "student_id": 2, "subject_id": 6, "period": "2024-весна", "current": 38, "final": 42},
    {"id": 17, "student_id": 2, "subject_id": 7, "period": "2024-весна", "current": 38, "final": 48},
    {"id": 18, "student_id": 2, "subject_id": 8, "period": "2024-весна", "current": 36, "final": 46},
    {"id": 19, "student_id": 2, "subject_id": 9, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 20, "student_id": 2, "subject_id": 10, "period": "2024-весна", "current": 38, "final": 45},
]

# === Гориченко (3) — отличник ===
GRADES_3 = [
    {"id": 21, "student_id": 3, "subject_id": 1, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 22, "student_id": 3, "subject_id": 2, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 23, "student_id": 3, "subject_id": 3, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 24, "student_id": 3, "subject_id": 4, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 25, "student_id": 3, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 55},
    {"id": 26, "student_id": 3, "subject_id": 6, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 27, "student_id": 3, "subject_id": 7, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 28, "student_id": 3, "subject_id": 8, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 29, "student_id": 3, "subject_id": 9, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 30, "student_id": 3, "subject_id": 10, "period": "2024-весна", "current": 40, "final": 60},
]

# === Жуковец (4) — средний ===
GRADES_4 = [
    {"id": 31, "student_id": 4, "subject_id": 1, "period": "2024-весна", "current": 32, "final": 38},
    {"id": 32, "student_id": 4, "subject_id": 2, "period": "2024-весна", "current": 35, "final": 45},
    {"id": 33, "student_id": 4, "subject_id": 3, "period": "2024-весна", "current": 33, "final": 40},
    {"id": 34, "student_id": 4, "subject_id": 4, "period": "2024-весна", "current": 34, "final": 42},
    {"id": 35, "student_id": 4, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 50},
    {"id": 36, "student_id": 4, "subject_id": 6, "period": "2024-весна", "current": 30, "final": 35},
    {"id": 37, "student_id": 4, "subject_id": 7, "period": "2024-весна", "current": 35, "final": 40},
    {"id": 38, "student_id": 4, "subject_id": 8, "period": "2024-весна", "current": 34, "final": 42},
    {"id": 39, "student_id": 4, "subject_id": 9, "period": "2024-весна", "current": 36, "final": 45},
    {"id": 40, "student_id": 4, "subject_id": 10, "period": "2024-весна", "current": 38, "final": 40},
]

# === Конопельный (5) — хорошист ===
GRADES_5 = [
    {"id": 41, "student_id": 5, "subject_id": 1, "period": "2024-весна", "current": 36, "final": 50},
    {"id": 42, "student_id": 5, "subject_id": 2, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 43, "student_id": 5, "subject_id": 3, "period": "2024-весна", "current": 38, "final": 48},
    {"id": 44, "student_id": 5, "subject_id": 4, "period": "2024-весна", "current": 40, "final": 55},
    {"id": 45, "student_id": 5, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 50},
    {"id": 46, "student_id": 5, "subject_id": 6, "period": "2024-весна", "current": 38, "final": 45},
    {"id": 47, "student_id": 5, "subject_id": 7, "period": "2024-весна", "current": 40, "final": 55},
    {"id": 48, "student_id": 5, "subject_id": 8, "period": "2024-весна", "current": 36, "final": 48},
    {"id": 49, "student_id": 5, "subject_id": 9, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 50, "student_id": 5, "subject_id": 10, "period": "2024-весна", "current": 38, "final": 45},
]

# === Косенков (6) — отличник ===
GRADES_6 = [
    {"id": 51, "student_id": 6, "subject_id": 1, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 52, "student_id": 6, "subject_id": 2, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 53, "student_id": 6, "subject_id": 3, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 54, "student_id": 6, "subject_id": 4, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 55, "student_id": 6, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 55},
    {"id": 56, "student_id": 6, "subject_id": 6, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 57, "student_id": 6, "subject_id": 7, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 58, "student_id": 6, "subject_id": 8, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 59, "student_id": 6, "subject_id": 9, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 60, "student_id": 6, "subject_id": 10, "period": "2024-весна", "current": 40, "final": 60},
]

# === Медведев (7) — средний ===
GRADES_7 = [
    {"id": 61, "student_id": 7, "subject_id": 1, "period": "2024-весна", "current": 32, "final": 35},
    {"id": 62, "student_id": 7, "subject_id": 2, "period": "2024-весна", "current": 35, "final": 42},
    {"id": 63, "student_id": 7, "subject_id": 3, "period": "2024-весна", "current": 30, "final": 35},
    {"id": 64, "student_id": 7, "subject_id": 4, "period": "2024-весна", "current": 34, "final": 40},
    {"id": 65, "student_id": 7, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 50},
    {"id": 66, "student_id": 7, "subject_id": 6, "period": "2024-весна", "current": 35, "final": 38},
    {"id": 67, "student_id": 7, "subject_id": 7, "period": "2024-весна", "current": 32, "final": 35},
    {"id": 68, "student_id": 7, "subject_id": 8, "period": "2024-весна", "current": 34, "final": 40},
    {"id": 69, "student_id": 7, "subject_id": 9, "period": "2024-весна", "current": 36, "final": 42},
    {"id": 70, "student_id": 7, "subject_id": 10, "period": "2024-весна", "current": 38, "final": 40},
]

# === Мельников (8) — троечник ===
GRADES_8 = [
    {"id": 71, "student_id": 8, "subject_id": 1, "period": "2024-весна", "current": 28, "final": 30},
    {"id": 72, "student_id": 8, "subject_id": 2, "period": "2024-весна", "current": 32, "final": 38},
    {"id": 73, "student_id": 8, "subject_id": 3, "period": "2024-весна", "current": 25, "final": 32},
    {"id": 74, "student_id": 8, "subject_id": 4, "period": "2024-весна", "current": 28, "final": 30},
    {"id": 75, "student_id": 8, "subject_id": 5, "period": "2024-весна", "current": 35, "final": 40},
    {"id": 76, "student_id": 8, "subject_id": 6, "period": "2024-весна", "current": 26, "final": 28},
    {"id": 77, "student_id": 8, "subject_id": 7, "period": "2024-весна", "current": 28, "final": 30},
    {"id": 78, "student_id": 8, "subject_id": 8, "period": "2024-весна", "current": 27, "final": 30},
    {"id": 79, "student_id": 8, "subject_id": 9, "period": "2024-весна", "current": 32, "final": 38},
    {"id": 80, "student_id": 8, "subject_id": 10, "period": "2024-весна", "current": 30, "final": 32},
]

# === Наконечный (9) — РЕАЛЬНЫЕ ДАННЫЕ ИЗ ЗАЧЁТКИ ===
GRADES_9 = [
    {"id": 81, "student_id": 9, "subject_id": 1, "period": "2024-весна", "current": 30, "final": 31},   # Архитектура — 61 (удовл)
    {"id": 82, "student_id": 9, "subject_id": 2, "period": "2024-весна", "current": 40, "final": 60},   # ИЯ — 100 (отлично)
    {"id": 83, "student_id": 9, "subject_id": 3, "period": "2024-весна", "current": 40, "final": 51},   # ИО — 91 (отлично)
    {"id": 84, "student_id": 9, "subject_id": 4, "period": "2024-весна", "current": 40, "final": 60},   # ОС — 100 (отлично)
    {"id": 85, "student_id": 9, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 44},   # Физкультура — 84 (зачтено)
    {"id": 86, "student_id": 9, "subject_id": 6, "period": "2024-весна", "current": 40, "final": 38},   # Java — 78 (хорошо)
    {"id": 87, "student_id": 9, "subject_id": 7, "period": "2024-весна", "current": 39, "final": 50},   # Проектная — 89 (зачтено)
    {"id": 88, "student_id": 9, "subject_id": 8, "period": "2024-весна", "current": 40, "final": 52},   # ТВиМС — 92 (отлично)
    {"id": 89, "student_id": 9, "subject_id": 9, "period": "2024-весна", "current": 38, "final": 60},   # Облака — 98 (зачтено)
    {"id": 90, "student_id": 9, "subject_id": 10, "period": "2024-весна", "current": 40, "final": 60},  # Практика — 100 (отлично)
]

# === Овсянников (10) — хорошист ===
GRADES_10 = [
    {"id": 91, "student_id": 10, "subject_id": 1, "period": "2024-весна", "current": 36, "final": 48},
    {"id": 92, "student_id": 10, "subject_id": 2, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 93, "student_id": 10, "subject_id": 3, "period": "2024-весна", "current": 37, "final": 46},
    {"id": 94, "student_id": 10, "subject_id": 4, "period": "2024-весна", "current": 36, "final": 48},
    {"id": 95, "student_id": 10, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 50},
    {"id": 96, "student_id": 10, "subject_id": 6, "period": "2024-весна", "current": 38, "final": 42},
    {"id": 97, "student_id": 10, "subject_id": 7, "period": "2024-весна", "current": 38, "final": 48},
    {"id": 98, "student_id": 10, "subject_id": 8, "period": "2024-весна", "current": 36, "final": 46},
    {"id": 99, "student_id": 10, "subject_id": 9, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 100, "student_id": 10, "subject_id": 10, "period": "2024-весна", "current": 38, "final": 45},
]

# === Пшенко (11) — отличница ===
GRADES_11 = [
    {"id": 101, "student_id": 11, "subject_id": 1, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 102, "student_id": 11, "subject_id": 2, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 103, "student_id": 11, "subject_id": 3, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 104, "student_id": 11, "subject_id": 4, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 105, "student_id": 11, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 55},
    {"id": 106, "student_id": 11, "subject_id": 6, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 107, "student_id": 11, "subject_id": 7, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 108, "student_id": 11, "subject_id": 8, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 109, "student_id": 11, "subject_id": 9, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 110, "student_id": 11, "subject_id": 10, "period": "2024-весна", "current": 40, "final": 60},
]

# === Сергеев (12) — средний ===
GRADES_12 = [
    {"id": 111, "student_id": 12, "subject_id": 1, "period": "2024-весна", "current": 34, "final": 40},
    {"id": 112, "student_id": 12, "subject_id": 2, "period": "2024-весна", "current": 36, "final": 42},
    {"id": 113, "student_id": 12, "subject_id": 3, "period": "2024-весна", "current": 35, "final": 40},
    {"id": 114, "student_id": 12, "subject_id": 4, "period": "2024-весна", "current": 32, "final": 35},
    {"id": 115, "student_id": 12, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 50},
    {"id": 116, "student_id": 12, "subject_id": 6, "period": "2024-весна", "current": 36, "final": 42},
    {"id": 117, "student_id": 12, "subject_id": 7, "period": "2024-весна", "current": 36, "final": 40},
    {"id": 118, "student_id": 12, "subject_id": 8, "period": "2024-весна", "current": 35, "final": 42},
    {"id": 119, "student_id": 12, "subject_id": 9, "period": "2024-весна", "current": 36, "final": 42},
    {"id": 120, "student_id": 12, "subject_id": 10, "period": "2024-весна", "current": 38, "final": 40},
]

# === Слесарчук (13) — хорошист ===
GRADES_13 = [
    {"id": 121, "student_id": 13, "subject_id": 1, "period": "2024-весна", "current": 37, "final": 48},
    {"id": 122, "student_id": 13, "subject_id": 2, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 123, "student_id": 13, "subject_id": 3, "period": "2024-весна", "current": 38, "final": 46},
    {"id": 124, "student_id": 13, "subject_id": 4, "period": "2024-весна", "current": 37, "final": 48},
    {"id": 125, "student_id": 13, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 50},
    {"id": 126, "student_id": 13, "subject_id": 6, "period": "2024-весна", "current": 38, "final": 44},
    {"id": 127, "student_id": 13, "subject_id": 7, "period": "2024-весна", "current": 38, "final": 48},
    {"id": 128, "student_id": 13, "subject_id": 8, "period": "2024-весна", "current": 40, "final": 55},
    {"id": 129, "student_id": 13, "subject_id": 9, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 130, "student_id": 13, "subject_id": 10, "period": "2024-весна", "current": 38, "final": 45},
]

# === Терещенко (14) — отличник ===
GRADES_14 = [
    {"id": 131, "student_id": 14, "subject_id": 1, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 132, "student_id": 14, "subject_id": 2, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 133, "student_id": 14, "subject_id": 3, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 134, "student_id": 14, "subject_id": 4, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 135, "student_id": 14, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 55},
    {"id": 136, "student_id": 14, "subject_id": 6, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 137, "student_id": 14, "subject_id": 7, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 138, "student_id": 14, "subject_id": 8, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 139, "student_id": 14, "subject_id": 9, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 140, "student_id": 14, "subject_id": 10, "period": "2024-весна", "current": 40, "final": 60},
]

# === Фоменко (15) — средний ===
GRADES_15 = [
    {"id": 141, "student_id": 15, "subject_id": 1, "period": "2024-весна", "current": 34, "final": 40},
    {"id": 142, "student_id": 15, "subject_id": 2, "period": "2024-весна", "current": 36, "final": 42},
    {"id": 143, "student_id": 15, "subject_id": 3, "period": "2024-весна", "current": 35, "final": 42},
    {"id": 144, "student_id": 15, "subject_id": 4, "period": "2024-весна", "current": 36, "final": 42},
    {"id": 145, "student_id": 15, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 50},
    {"id": 146, "student_id": 15, "subject_id": 6, "period": "2024-весна", "current": 32, "final": 35},
    {"id": 147, "student_id": 15, "subject_id": 7, "period": "2024-весна", "current": 36, "final": 40},
    {"id": 148, "student_id": 15, "subject_id": 8, "period": "2024-весна", "current": 35, "final": 42},
    {"id": 149, "student_id": 15, "subject_id": 9, "period": "2024-весна", "current": 36, "final": 42},
    {"id": 150, "student_id": 15, "subject_id": 10, "period": "2024-весна", "current": 38, "final": 40},
]

# === Холодилин (16) — хорошист ===
GRADES_16 = [
    {"id": 151, "student_id": 16, "subject_id": 1, "period": "2024-весна", "current": 36, "final": 48},
    {"id": 152, "student_id": 16, "subject_id": 2, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 153, "student_id": 16, "subject_id": 3, "period": "2024-весна", "current": 37, "final": 46},
    {"id": 154, "student_id": 16, "subject_id": 4, "period": "2024-весна", "current": 36, "final": 48},
    {"id": 155, "student_id": 16, "subject_id": 5, "period": "2024-весна", "current": 40, "final": 50},
    {"id": 156, "student_id": 16, "subject_id": 6, "period": "2024-весна", "current": 38, "final": 44},
    {"id": 157, "student_id": 16, "subject_id": 7, "period": "2024-весна", "current": 38, "final": 48},
    {"id": 158, "student_id": 16, "subject_id": 8, "period": "2024-весна", "current": 36, "final": 46},
    {"id": 159, "student_id": 16, "subject_id": 9, "period": "2024-весна", "current": 40, "final": 60},
    {"id": 160, "student_id": 16, "subject_id": 10, "period": "2024-весна", "current": 38, "final": 45},
]

# ==================== 2023-ОСЕНЬ (для динамики) ====================

# Наконечный (9) — на балл ниже
GRADES_9_OLD = [
    {"id": 201, "student_id": 9, "subject_id": 1, "period": "2023-осень", "current": 35, "final": 40},
    {"id": 202, "student_id": 9, "subject_id": 2, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 203, "student_id": 9, "subject_id": 3, "period": "2023-осень", "current": 38, "final": 45},
    {"id": 204, "student_id": 9, "subject_id": 4, "period": "2023-осень", "current": 38, "final": 48},
    {"id": 205, "student_id": 9, "subject_id": 5, "period": "2023-осень", "current": 40, "final": 50},
    {"id": 206, "student_id": 9, "subject_id": 6, "period": "2023-осень", "current": 35, "final": 38},
    {"id": 207, "student_id": 9, "subject_id": 7, "period": "2023-осень", "current": 36, "final": 42},
    {"id": 208, "student_id": 9, "subject_id": 8, "period": "2023-осень", "current": 36, "final": 45},
    {"id": 209, "student_id": 9, "subject_id": 9, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 210, "student_id": 9, "subject_id": 10, "period": "2023-осень", "current": 38, "final": 45},
]

# Мельников (8) — троечник
GRADES_8_OLD = [
    {"id": 211, "student_id": 8, "subject_id": 1, "period": "2023-осень", "current": 25, "final": 28},
    {"id": 212, "student_id": 8, "subject_id": 2, "period": "2023-осень", "current": 30, "final": 35},
    {"id": 213, "student_id": 8, "subject_id": 3, "period": "2023-осень", "current": 22, "final": 28},
    {"id": 214, "student_id": 8, "subject_id": 4, "period": "2023-осень", "current": 25, "final": 28},
    {"id": 215, "student_id": 8, "subject_id": 5, "period": "2023-осень", "current": 32, "final": 38},
    {"id": 216, "student_id": 8, "subject_id": 6, "period": "2023-осень", "current": 24, "final": 26},
    {"id": 217, "student_id": 8, "subject_id": 7, "period": "2023-осень", "current": 26, "final": 28},
    {"id": 218, "student_id": 8, "subject_id": 8, "period": "2023-осень", "current": 25, "final": 28},
    {"id": 219, "student_id": 8, "subject_id": 9, "period": "2023-осень", "current": 30, "final": 35},
    {"id": 220, "student_id": 8, "subject_id": 10, "period": "2023-осень", "current": 28, "final": 30},
]

# Анисимов (1) — отличник
GRADES_1_OLD = [
    {"id": 221, "student_id": 1, "subject_id": 1, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 222, "student_id": 1, "subject_id": 2, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 223, "student_id": 1, "subject_id": 3, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 224, "student_id": 1, "subject_id": 4, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 225, "student_id": 1, "subject_id": 5, "period": "2023-осень", "current": 40, "final": 55},
    {"id": 226, "student_id": 1, "subject_id": 6, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 227, "student_id": 1, "subject_id": 7, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 228, "student_id": 1, "subject_id": 8, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 229, "student_id": 1, "subject_id": 9, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 230, "student_id": 1, "subject_id": 10, "period": "2023-осень", "current": 40, "final": 60},
]

# Горин (2) — хорошист
GRADES_2_OLD = [
    {"id": 231, "student_id": 2, "subject_id": 1, "period": "2023-осень", "current": 34, "final": 45},
    {"id": 232, "student_id": 2, "subject_id": 2, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 233, "student_id": 2, "subject_id": 3, "period": "2023-осень", "current": 35, "final": 42},
    {"id": 234, "student_id": 2, "subject_id": 4, "period": "2023-осень", "current": 34, "final": 45},
    {"id": 235, "student_id": 2, "subject_id": 5, "period": "2023-осень", "current": 40, "final": 50},
    {"id": 236, "student_id": 2, "subject_id": 6, "period": "2023-осень", "current": 36, "final": 40},
    {"id": 237, "student_id": 2, "subject_id": 7, "period": "2023-осень", "current": 36, "final": 45},
    {"id": 238, "student_id": 2, "subject_id": 8, "period": "2023-осень", "current": 35, "final": 42},
    {"id": 239, "student_id": 2, "subject_id": 9, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 240, "student_id": 2, "subject_id": 10, "period": "2023-осень", "current": 36, "final": 42},
]

# Гориченко (3) — отличник
GRADES_3_OLD = [
    {"id": 241, "student_id": 3, "subject_id": 1, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 242, "student_id": 3, "subject_id": 2, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 243, "student_id": 3, "subject_id": 3, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 244, "student_id": 3, "subject_id": 4, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 245, "student_id": 3, "subject_id": 5, "period": "2023-осень", "current": 40, "final": 55},
    {"id": 246, "student_id": 3, "subject_id": 6, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 247, "student_id": 3, "subject_id": 7, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 248, "student_id": 3, "subject_id": 8, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 249, "student_id": 3, "subject_id": 9, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 250, "student_id": 3, "subject_id": 10, "period": "2023-осень", "current": 40, "final": 60},
]

# Жуковец (4) — средний
GRADES_4_OLD = [
    {"id": 251, "student_id": 4, "subject_id": 1, "period": "2023-осень", "current": 30, "final": 35},
    {"id": 252, "student_id": 4, "subject_id": 2, "period": "2023-осень", "current": 32, "final": 40},
    {"id": 253, "student_id": 4, "subject_id": 3, "period": "2023-осень", "current": 30, "final": 35},
    {"id": 254, "student_id": 4, "subject_id": 4, "period": "2023-осень", "current": 31, "final": 38},
    {"id": 255, "student_id": 4, "subject_id": 5, "period": "2023-осень", "current": 38, "final": 45},
    {"id": 256, "student_id": 4, "subject_id": 6, "period": "2023-осень", "current": 28, "final": 30},
    {"id": 257, "student_id": 4, "subject_id": 7, "period": "2023-осень", "current": 32, "final": 35},
    {"id": 258, "student_id": 4, "subject_id": 8, "period": "2023-осень", "current": 31, "final": 38},
    {"id": 259, "student_id": 4, "subject_id": 9, "period": "2023-осень", "current": 34, "final": 40},
    {"id": 260, "student_id": 4, "subject_id": 10, "period": "2023-осень", "current": 35, "final": 38},
]

# Конопельный (5) — хорошист
GRADES_5_OLD = [
    {"id": 261, "student_id": 5, "subject_id": 1, "period": "2023-осень", "current": 34, "final": 45},
    {"id": 262, "student_id": 5, "subject_id": 2, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 263, "student_id": 5, "subject_id": 3, "period": "2023-осень", "current": 36, "final": 45},
    {"id": 264, "student_id": 5, "subject_id": 4, "period": "2023-осень", "current": 38, "final": 50},
    {"id": 265, "student_id": 5, "subject_id": 5, "period": "2023-осень", "current": 40, "final": 50},
    {"id": 266, "student_id": 5, "subject_id": 6, "period": "2023-осень", "current": 36, "final": 42},
    {"id": 267, "student_id": 5, "subject_id": 7, "period": "2023-осень", "current": 38, "final": 50},
    {"id": 268, "student_id": 5, "subject_id": 8, "period": "2023-осень", "current": 34, "final": 45},
    {"id": 269, "student_id": 5, "subject_id": 9, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 270, "student_id": 5, "subject_id": 10, "period": "2023-осень", "current": 36, "final": 42},
]

# Косенков (6) — отличник
GRADES_6_OLD = [
    {"id": 271, "student_id": 6, "subject_id": 1, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 272, "student_id": 6, "subject_id": 2, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 273, "student_id": 6, "subject_id": 3, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 274, "student_id": 6, "subject_id": 4, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 275, "student_id": 6, "subject_id": 5, "period": "2023-осень", "current": 40, "final": 55},
    {"id": 276, "student_id": 6, "subject_id": 6, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 277, "student_id": 6, "subject_id": 7, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 278, "student_id": 6, "subject_id": 8, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 279, "student_id": 6, "subject_id": 9, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 280, "student_id": 6, "subject_id": 10, "period": "2023-осень", "current": 40, "final": 60},
]

# Медведев (7) — средний
GRADES_7_OLD = [
    {"id": 281, "student_id": 7, "subject_id": 1, "period": "2023-осень", "current": 30, "final": 32},
    {"id": 282, "student_id": 7, "subject_id": 2, "period": "2023-осень", "current": 32, "final": 38},
    {"id": 283, "student_id": 7, "subject_id": 3, "period": "2023-осень", "current": 28, "final": 32},
    {"id": 284, "student_id": 7, "subject_id": 4, "period": "2023-осень", "current": 31, "final": 35},
    {"id": 285, "student_id": 7, "subject_id": 5, "period": "2023-осень", "current": 38, "final": 45},
    {"id": 286, "student_id": 7, "subject_id": 6, "period": "2023-осень", "current": 32, "final": 35},
    {"id": 287, "student_id": 7, "subject_id": 7, "period": "2023-осень", "current": 30, "final": 32},
    {"id": 288, "student_id": 7, "subject_id": 8, "period": "2023-осень", "current": 31, "final": 35},
    {"id": 289, "student_id": 7, "subject_id": 9, "period": "2023-осень", "current": 33, "final": 38},
    {"id": 290, "student_id": 7, "subject_id": 10, "period": "2023-осень", "current": 35, "final": 38},
]

# Овсянников (10) — хорошист
GRADES_10_OLD = [
    {"id": 291, "student_id": 10, "subject_id": 1, "period": "2023-осень", "current": 34, "final": 45},
    {"id": 292, "student_id": 10, "subject_id": 2, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 293, "student_id": 10, "subject_id": 3, "period": "2023-осень", "current": 35, "final": 42},
    {"id": 294, "student_id": 10, "subject_id": 4, "period": "2023-осень", "current": 34, "final": 45},
    {"id": 295, "student_id": 10, "subject_id": 5, "period": "2023-осень", "current": 40, "final": 50},
    {"id": 296, "student_id": 10, "subject_id": 6, "period": "2023-осень", "current": 36, "final": 40},
    {"id": 297, "student_id": 10, "subject_id": 7, "period": "2023-осень", "current": 36, "final": 45},
    {"id": 298, "student_id": 10, "subject_id": 8, "period": "2023-осень", "current": 35, "final": 42},
    {"id": 299, "student_id": 10, "subject_id": 9, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 300, "student_id": 10, "subject_id": 10, "period": "2023-осень", "current": 36, "final": 42},
]

# Пшенко (11) — отличница
GRADES_11_OLD = [
    {"id": 301, "student_id": 11, "subject_id": 1, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 302, "student_id": 11, "subject_id": 2, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 303, "student_id": 11, "subject_id": 3, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 304, "student_id": 11, "subject_id": 4, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 305, "student_id": 11, "subject_id": 5, "period": "2023-осень", "current": 40, "final": 55},
    {"id": 306, "student_id": 11, "subject_id": 6, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 307, "student_id": 11, "subject_id": 7, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 308, "student_id": 11, "subject_id": 8, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 309, "student_id": 11, "subject_id": 9, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 310, "student_id": 11, "subject_id": 10, "period": "2023-осень", "current": 40, "final": 60},
]

# Сергеев (12) — средний
GRADES_12_OLD = [
    {"id": 311, "student_id": 12, "subject_id": 1, "period": "2023-осень", "current": 32, "final": 35},
    {"id": 312, "student_id": 12, "subject_id": 2, "period": "2023-осень", "current": 34, "final": 40},
    {"id": 313, "student_id": 12, "subject_id": 3, "period": "2023-осень", "current": 33, "final": 38},
    {"id": 314, "student_id": 12, "subject_id": 4, "period": "2023-осень", "current": 30, "final": 32},
    {"id": 315, "student_id": 12, "subject_id": 5, "period": "2023-осень", "current": 38, "final": 45},
    {"id": 316, "student_id": 12, "subject_id": 6, "period": "2023-осень", "current": 34, "final": 38},
    {"id": 317, "student_id": 12, "subject_id": 7, "period": "2023-осень", "current": 34, "final": 38},
    {"id": 318, "student_id": 12, "subject_id": 8, "period": "2023-осень", "current": 33, "final": 38},
    {"id": 319, "student_id": 12, "subject_id": 9, "period": "2023-осень", "current": 34, "final": 40},
    {"id": 320, "student_id": 12, "subject_id": 10, "period": "2023-осень", "current": 36, "final": 38},
]

# Слесарчук (13) — хорошист
GRADES_13_OLD = [
    {"id": 321, "student_id": 13, "subject_id": 1, "period": "2023-осень", "current": 35, "final": 45},
    {"id": 322, "student_id": 13, "subject_id": 2, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 323, "student_id": 13, "subject_id": 3, "period": "2023-осень", "current": 36, "final": 42},
    {"id": 324, "student_id": 13, "subject_id": 4, "period": "2023-осень", "current": 35, "final": 45},
    {"id": 325, "student_id": 13, "subject_id": 5, "period": "2023-осень", "current": 40, "final": 50},
    {"id": 326, "student_id": 13, "subject_id": 6, "period": "2023-осень", "current": 36, "final": 40},
    {"id": 327, "student_id": 13, "subject_id": 7, "period": "2023-осень", "current": 36, "final": 45},
    {"id": 328, "student_id": 13, "subject_id": 8, "period": "2023-осень", "current": 38, "final": 50},
    {"id": 329, "student_id": 13, "subject_id": 9, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 330, "student_id": 13, "subject_id": 10, "period": "2023-осень", "current": 36, "final": 42},
]

# Терещенко (14) — отличник
GRADES_14_OLD = [
    {"id": 331, "student_id": 14, "subject_id": 1, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 332, "student_id": 14, "subject_id": 2, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 333, "student_id": 14, "subject_id": 3, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 334, "student_id": 14, "subject_id": 4, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 335, "student_id": 14, "subject_id": 5, "period": "2023-осень", "current": 40, "final": 55},
    {"id": 336, "student_id": 14, "subject_id": 6, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 337, "student_id": 14, "subject_id": 7, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 338, "student_id": 14, "subject_id": 8, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 339, "student_id": 14, "subject_id": 9, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 340, "student_id": 14, "subject_id": 10, "period": "2023-осень", "current": 40, "final": 60},
]

# Фоменко (15) — средний
GRADES_15_OLD = [
    {"id": 341, "student_id": 15, "subject_id": 1, "period": "2023-осень", "current": 32, "final": 35},
    {"id": 342, "student_id": 15, "subject_id": 2, "period": "2023-осень", "current": 34, "final": 40},
    {"id": 343, "student_id": 15, "subject_id": 3, "period": "2023-осень", "current": 33, "final": 38},
    {"id": 344, "student_id": 15, "subject_id": 4, "period": "2023-осень", "current": 34, "final": 40},
    {"id": 345, "student_id": 15, "subject_id": 5, "period": "2023-осень", "current": 38, "final": 45},
    {"id": 346, "student_id": 15, "subject_id": 6, "period": "2023-осень", "current": 30, "final": 32},
    {"id": 347, "student_id": 15, "subject_id": 7, "period": "2023-осень", "current": 34, "final": 38},
    {"id": 348, "student_id": 15, "subject_id": 8, "period": "2023-осень", "current": 33, "final": 38},
    {"id": 349, "student_id": 15, "subject_id": 9, "period": "2023-осень", "current": 34, "final": 40},
    {"id": 350, "student_id": 15, "subject_id": 10, "period": "2023-осень", "current": 36, "final": 38},
]

# Холодилин (16) — хорошист
GRADES_16_OLD = [
    {"id": 351, "student_id": 16, "subject_id": 1, "period": "2023-осень", "current": 34, "final": 45},
    {"id": 352, "student_id": 16, "subject_id": 2, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 353, "student_id": 16, "subject_id": 3, "period": "2023-осень", "current": 35, "final": 42},
    {"id": 354, "student_id": 16, "subject_id": 4, "period": "2023-осень", "current": 34, "final": 45},
    {"id": 355, "student_id": 16, "subject_id": 5, "period": "2023-осень", "current": 40, "final": 50},
    {"id": 356, "student_id": 16, "subject_id": 6, "period": "2023-осень", "current": 36, "final": 40},
    {"id": 357, "student_id": 16, "subject_id": 7, "period": "2023-осень", "current": 36, "final": 45},
    {"id": 358, "student_id": 16, "subject_id": 8, "period": "2023-осень", "current": 35, "final": 42},
    {"id": 359, "student_id": 16, "subject_id": 9, "period": "2023-осень", "current": 40, "final": 60},
    {"id": 360, "student_id": 16, "subject_id": 10, "period": "2023-осень", "current": 36, "final": 42},
]

DEFAULT_GRADES = (
        GRADES_1 + GRADES_2 + GRADES_3 + GRADES_4 + GRADES_5 +
        GRADES_6 + GRADES_7 + GRADES_8 + GRADES_9 + GRADES_10 +
        GRADES_11 + GRADES_12 + GRADES_13 + GRADES_14 + GRADES_15 + GRADES_16 +
        GRADES_1_OLD + GRADES_2_OLD + GRADES_3_OLD + GRADES_4_OLD + GRADES_5_OLD +
        GRADES_6_OLD + GRADES_7_OLD + GRADES_8_OLD + GRADES_9_OLD + GRADES_10_OLD +
        GRADES_11_OLD + GRADES_12_OLD + GRADES_13_OLD + GRADES_14_OLD + GRADES_15_OLD + GRADES_16_OLD
)


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