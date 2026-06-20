from typing import List, Dict
import statistics


def calculate_weighted_rating(
        student_id: int,
        grades: List[Dict],
        subjects: List[Dict]
) -> float:
    """
    Взвешенное среднее арифметическое оценок студента.
    Формула: sum(value_i * weight_i) / sum(weight_i)
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
        value = g.get("value", 0)
        weighted_sum += value * weight
        total_weight += weight

    return round(weighted_sum / total_weight, 2) if total_weight > 0 else 0.0


def calculate_group_average(grades: List[Dict], subjects: List[Dict]) -> float:
    """Средний взвешенный балл по всей группе."""
    student_ids = {g["student_id"] for g in grades}
    if not student_ids:
        return 0.0
    ratings = [calculate_weighted_rating(sid, grades, subjects) for sid in student_ids]
    return round(statistics.mean(ratings), 2)