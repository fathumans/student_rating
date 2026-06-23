from typing import List, Dict
import statistics
from .aggregator import calculate_absolute_rating, calculate_weighted_rating


def compare_periods(
        grades: List[Dict],
        subjects: List[Dict],
        period1: str,
        period2: str
) -> Dict:
    """
    Сравнение группы между двумя периодами: абсолютный и взвешенный рейтинг.
    """
    def _avg_for_period(p: str, weighted: bool = False) -> float:
        p_grades = [g for g in grades if g.get("period") == p]
        sids = {g["student_id"] for g in p_grades}
        if not sids:
            return 0.0
        if weighted:
            ratings = [calculate_weighted_rating(sid, p_grades, subjects) for sid in sids]
        else:
            ratings = [calculate_absolute_rating(sid, p_grades, subjects) for sid in sids]
        return round(statistics.mean(ratings), 2)

    abs1 = _avg_for_period(period1, weighted=False)
    abs2 = _avg_for_period(period2, weighted=False)
    w1 = _avg_for_period(period1, weighted=True)
    w2 = _avg_for_period(period2, weighted=True)

    return {
        "period1": period1,
        "period2": period2,
        "absolute": {
            "average1": abs1,
            "average2": abs2,
            "delta": round(abs2 - abs1, 2),
            "trend": "рост" if abs2 > abs1 else ("падение" if abs2 < abs1 else "стабильность")
        },
        "weighted": {
            "average1": w1,
            "average2": w2,
            "delta": round(w2 - w1, 2),
            "trend": "рост" if w2 > w1 else ("падение" if w2 < w1 else "стабильность")
        }
    }


def student_dynamics(
        student_id: int,
        grades: List[Dict],
        subjects: List[Dict]
) -> List[Dict]:
    """Динамика конкретного студента по периодам (оба рейтинга)."""
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
        result.append({
            "period": p,
            "absolute_rating": calculate_absolute_rating(student_id, p_grades, subjects),
            "weighted_rating": calculate_weighted_rating(student_id, p_grades, subjects),
            "subjects_count": len(p_grades),
        })
    return result