from typing import List, Dict
import statistics
from .aggregator import calculate_weighted_rating


def find_problem_subjects(
        grades: List[Dict],
        subjects: List[Dict],
        threshold: float = 0.15
) -> List[Dict]:
    """
    Предметы, где доля неудовлетворительных оценок (<=3)
    превышает заданный порог (по умолчанию 15%).
    """
    problems = []
    for subj in subjects:
        sid = subj["id"]
        subj_grades = [g["value"] for g in grades if g.get("subject_id") == sid]
        if not subj_grades:
            continue
        bad_count = sum(1 for v in subj_grades if v <= 3)
        bad_rate = bad_count / len(subj_grades)
        if bad_rate > threshold:
            problems.append({
                "subject_id": sid,
                "subject_name": subj.get("name", "Unknown"),
                "bad_rate": round(bad_rate, 2),
                "average": round(statistics.mean(subj_grades), 2),
                "total_students": len(subj_grades)
            })
    return problems


def find_problem_students(
        students: List[Dict],
        grades: List[Dict],
        subjects: List[Dict],
        threshold: float = 2.0
) -> List[Dict]:
    """Студенты со средним взвешенным баллом ниже порога."""
    result = []
    for s in students:
        rating = calculate_weighted_rating(s["id"], grades, subjects)
        if rating < threshold:
            result.append({**s, "rating": rating})
    return result