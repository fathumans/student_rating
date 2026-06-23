from typing import List, Dict
import statistics
from .converter import score_to_grade, score_to_status

def calculate_subject_total(grade_entry: Dict) -> float:
    """Итоговый балл за предмет: текущая + промежуточная (макс 100)."""
    current = grade_entry.get("current", 0) or 0
    final = grade_entry.get("final", 0) or 0
    return min(current + final, 100)


def calculate_absolute_rating(
        student_id: int,
        grades: List[Dict],
        subjects: List[Dict]
) -> float:
    """
    Абсолютный рейтинг: простое среднее итоговых баллов.
    Формула: Σ(total_score) / N
    """
    student_grades = [
        calculate_subject_total(g)
        for g in grades
        if g.get("student_id") == student_id
    ]
    if not student_grades:
        return 0.0
    return round(statistics.mean(student_grades), 2)


def calculate_weighted_rating(
        student_id: int,
        grades: List[Dict],
        subjects: List[Dict]
) -> float:
    """
    Взвешенный рейтинг: среднее с учётом типа предмета.
    Формула: Σ(total_score × weight) / Σ(weight)
    """
    subject_map = {s["id"]: s for s in subjects}
    weighted_sum = 0.0
    total_weight = 0.0

    for g in grades:
        if g.get("student_id") != student_id:
            continue
        subj = subject_map.get(g.get("subject_id"))
        if not subj:
            continue
        weight = subj.get("weight", 1.0)
        score = calculate_subject_total(g)
        weighted_sum += score * weight
        total_weight += weight

    return round(weighted_sum / total_weight, 2) if total_weight > 0 else 0.0


def calculate_group_average_absolute(grades: List[Dict], subjects: List[Dict]) -> float:
    """Средний абсолютный балл по всей группе."""
    student_ids = {g["student_id"] for g in grades}
    if not student_ids:
        return 0.0
    ratings = [calculate_absolute_rating(sid, grades, subjects) for sid in student_ids]
    return round(statistics.mean(ratings), 2)


def calculate_group_average_weighted(grades: List[Dict], subjects: List[Dict]) -> float:
    """Средний взвешенный балл по всей группе."""
    student_ids = {g["student_id"] for g in grades}
    if not student_ids:
        return 0.0
    ratings = [calculate_weighted_rating(sid, grades, subjects) for sid in student_ids]
    return round(statistics.mean(ratings), 2)


def get_student_subjects_detail(
        student_id: int,
        grades: List[Dict],
        subjects: List[Dict]
) -> List[Dict]:
    """
    Детализация по предметам для студента.
    Возвращает: предмет, current, final, total, grade, status, weight
    """
    subject_map = {s["id"]: s for s in subjects}
    result = []
    for g in grades:
        if g.get("student_id") != student_id:
            continue
        subj = subject_map.get(g.get("subject_id"))
        if not subj:
            continue
        total = calculate_subject_total(g)
        result.append({
            "subject_id": subj["id"],
            "subject_name": subj["name"],
            "type": subj["type"],
            "weight": subj["weight"],
            "current": g.get("current", 0),
            "final": g.get("final", 0),
            "total_score": total,
            "grade": score_to_grade(total),
            "status": score_to_status(total),
        })
    return result