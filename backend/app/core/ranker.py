from typing import List, Dict
from .aggregator import calculate_absolute_rating, calculate_weighted_rating


def rank_students_absolute(
        students: List[Dict],
        grades: List[Dict],
        subjects: List[Dict]
) -> List[Dict]:
    def count_excellent(student_id: int) -> int:
        from .aggregator import calculate_subject_total
        return sum(
            1 for g in grades
            if g.get("student_id") == student_id and calculate_subject_total(g) >= 91
        )

    enriched = []
    for s in students:
        sid = s["id"]
        enriched.append({
            **s,
            "absolute_rating": calculate_absolute_rating(sid, grades, subjects),
            "excellent_count": count_excellent(sid),
        })

    enriched.sort(
        key=lambda x: (-x["absolute_rating"], -x["excellent_count"], x.get("name", ""))
    )

    for idx, item in enumerate(enriched, 1):
        item["absolute_rank"] = idx

    return enriched

def rank_students_weighted(
        students: List[Dict],
        grades: List[Dict],
        subjects: List[Dict]
) -> List[Dict]:
    subject_map = {s["id"]: s for s in subjects}

    def count_excellent_exams(student_id: int) -> int:
        from .aggregator import calculate_subject_total
        return sum(
            1 for g in grades
            if g.get("student_id") == student_id
            and calculate_subject_total(g) >= 91
            and subject_map.get(g.get("subject_id"), {}).get("type") == "exam"
        )

    enriched = []
    for s in students:
        sid = s["id"]
        enriched.append({
            **s,
            "weighted_rating": calculate_weighted_rating(sid, grades, subjects),
            "excellent_exams_count": count_excellent_exams(sid),
        })

    enriched.sort(
        key=lambda x: (-x["weighted_rating"], -x["excellent_exams_count"], x.get("name", ""))
    )

    for idx, item in enumerate(enriched, 1):
        item["weighted_rank"] = idx

    return enriched


def get_combined_ranking(students, grades, subjects):
    abs_ranked = {item["id"]: item for item in rank_students_absolute(students, grades, subjects)}
    w_ranked = {item["id"]: item for item in rank_students_weighted(students, grades, subjects)}

    result = []
    for s in students:
        sid = s["id"]
        abs_data = abs_ranked.get(sid, {})
        w_data = w_ranked.get(sid, {})
        result.append({
            **s,
            "absolute_rating": abs_data.get("absolute_rating", 0),
            "absolute_rank": abs_data.get("absolute_rank", 0),
            "weighted_rating": w_data.get("weighted_rating", 0),
            "weighted_rank": w_data.get("weighted_rank", 0),
            "rating_diff": abs_data.get("absolute_rank", 0) - w_data.get("weighted_rank", 0),
        })
    return result
