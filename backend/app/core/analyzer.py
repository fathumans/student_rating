from typing import List, Dict
import statistics
from .aggregator import calculate_subject_total


def find_problem_subjects(
        grades: List[Dict],
        subjects: List[Dict],
        threshold: float = 0.20
) -> List[Dict]:
    """
    Предметы, где > threshold доля студентов имеет <61 балл (неудовлетворительно).
    """
    problems = []
    for subj in subjects:
        sid = subj["id"]
        subj_scores = [
            calculate_subject_total(g)
            for g in grades
            if g.get("subject_id") == sid
        ]
        if not subj_scores:
            continue
        bad_count = sum(1 for score in subj_scores if score < 61)
        bad_rate = bad_count / len(subj_scores)
        if bad_rate > threshold:
            problems.append({
                "subject_id": sid,
                "subject_name": subj.get("name", "Unknown"),
                "bad_rate": round(bad_rate, 2),
                "average_score": round(statistics.mean(subj_scores), 2),
                "min_score": min(subj_scores),
                "max_score": max(subj_scores),
                "total_students": len(subj_scores),
            })
    return problems


def find_problem_students(
        students: List[Dict],
        grades: List[Dict],
        subjects: List[Dict],
        threshold: float = 61.0
) -> List[Dict]:
    """Студенты со средним абсолютным баллом ниже порога."""
    from .aggregator import calculate_absolute_rating
    result = []
    for s in students:
        rating = calculate_absolute_rating(s["id"], grades, subjects)
        if rating < threshold:
            result.append({
                **s,
                "absolute_rating": rating,
                "status": "Проблемная успеваемость" if rating < 61 else "Ниже среднего"
            })
    return result


def get_subject_statistics(grades: List[Dict], subjects: List[Dict]) -> List[Dict]:
    """Статистика по каждому предмету: средний, медиана, дисперсия."""
    result = []
    for subj in subjects:
        sid = subj["id"]
        scores = [
            calculate_subject_total(g)
            for g in grades
            if g.get("subject_id") == sid
        ]
        if not scores:
            continue
        result.append({
            "subject_id": sid,
            "subject_name": subj["name"],
            "average": round(statistics.mean(scores), 2),
            "median": round(statistics.median(scores), 2),
            "std_dev": round(statistics.stdev(scores), 2) if len(scores) > 1 else 0,
            "min": min(scores),
            "max": max(scores),
        })
    return result