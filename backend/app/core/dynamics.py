from typing import List, Dict
import statistics
from .aggregator import calculate_weighted_rating


def compare_periods(
        grades: List[Dict],
        subjects: List[Dict],
        period1: str,
        period2: str
) -> Dict:
    """
    Сравнение среднего балла группы между двумя периодами.
    Возвращает дельту и тренд (рост / падение / стабильность).
    """
    def _avg_for_period(p: str) -> float:
        p_grades = [g for g in grades if g.get("period") == p]
        sids = {g["student_id"] for g in p_grades}
        if not sids:
            return 0.0
        ratings = [calculate_weighted_rating(sid, p_grades, subjects) for sid in sids]
        return round(statistics.mean(ratings), 2)

    avg1 = _avg_for_period(period1)
    avg2 = _avg_for_period(period2)

    return {
        "period1": period1,
        "period2": period2,
        "average1": avg1,
        "average2": avg2,
        "delta": round(avg2 - avg1, 2),
        "trend": "рост" if avg2 > avg1 else ("падение" if avg2 < avg1 else "стабильность")
    }


def student_dynamics(
        student_id: int,
        grades: List[Dict],
        subjects: List[Dict]
) -> List[Dict]:
    """Динамика конкретного студента по семестрам/периодам."""
    periods = sorted({
        g.get("period")
        for g in grades
        if g.get("student_id") == student_id
    })
    result = []
    for p in periods:
        p_grades = [
            g for g in grades
            if g.get("student_id") == student_id and g.get("period") == p
        ]
        rating = calculate_weighted_rating(student_id, p_grades, subjects)
        result.append({
            "period": p,
            "rating": rating,
            "grades_count": len(p_grades)
        })
    return result