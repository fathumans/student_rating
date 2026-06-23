from typing import Dict, List


def score_to_grade(score: float) -> int:
    """
    Переводит итоговый балл (0-100) в оценку по 5-балльной шкале.
    91-100 → 5 (отлично)
    76-90  → 4 (хорошо)
    61-75  → 3 (удовлетворительно)
    ≤60    → 2 (неудовлетворительно)
    """
    if score >= 91:
        return 5
    elif score >= 76:
        return 4
    elif score >= 61:
        return 3
    else:
        return 2


def score_to_status(score: float) -> str:
    """Текстовое представление статуса."""
    grade = score_to_grade(score)
    mapping = {5: "Отлично", 4: "Хорошо", 3: "Удовлетворительно", 2: "Неудовлетворительно"}
    return mapping[grade]


def score_to_color(score: float) -> str:
    """Цвет для UI."""
    if score >= 91:
        return "#16a34a"  # зелёный
    elif score >= 76:
        return "#2563eb"  # синий
    elif score >= 61:
        return "#ca8a04"  # жёлтый
    else:
        return "#dc2626"  # красный


def convert_student_grades(grades: List[Dict]) -> List[Dict]:
    """
    Обогащает список оценок полями: total_score, grade, status.
    grades: [{"student_id": 1, "subject_id": 1, "current": 35, "final": 45, ...}, ...]
    """
    result = []
    for g in grades:
        current = g.get("current", 0) or 0
        final = g.get("final", 0) or 0
        total = min(current + final, 100)  # не более 100
        result.append({
            **g,
            "total_score": total,
            "grade": score_to_grade(total),
            "status": score_to_status(total),
        })
    return result