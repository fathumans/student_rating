from typing import List, Dict
from .aggregator import calculate_weighted_rating


def rank_students(
        students: List[Dict],
        grades: List[Dict],
        subjects: List[Dict]
) -> List[Dict]:
    """
    Ранжирование студентов по убыванию взвешенного рейтинга.
    При равенстве рейтинга: больше пятёрок -> выше.
    При равенстве пятёрок: алфавитный порядок фамилии.
    """
    def count_fives(student_id: int) -> int:
        return sum(
            1 for g in grades
            if g.get("student_id") == student_id and g.get("value") == 5
        )

    enriched = []
    for s in students:
        sid = s["id"]
        enriched.append({
            **s,
            "rating": calculate_weighted_rating(sid, grades, subjects),
            "fives_count": count_fives(sid)
        })

    enriched.sort(
        key=lambda x: (-x["rating"], -x["fives_count"], x.get("name", ""))
    )

    for idx, item in enumerate(enriched, 1):
        item["rank"] = idx

    return enriched