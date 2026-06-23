from app.core.dynamics import compare_periods, student_dynamics

SUBJECTS = [
    {"id": 1, "name": "Архитектура", "type": "exam", "weight": 1.0},
    {"id": 2, "name": "ИЯ", "type": "test", "weight": 0.6},
]


def test_compare_periods_growth():
    grades = [
        # 2023-осень
        {"student_id": 1, "subject_id": 1, "period": "2023-осень", "current": 35, "final": 40},
        {"student_id": 1, "subject_id": 2, "period": "2023-осень", "current": 40, "final": 60},
        {"student_id": 2, "subject_id": 1, "period": "2023-осень", "current": 30, "final": 35},
        {"student_id": 2, "subject_id": 2, "period": "2023-осень", "current": 35, "final": 45},
        # 2024-весна
        {"student_id": 1, "subject_id": 1, "period": "2024-весна", "current": 38, "final": 55},
        {"student_id": 1, "subject_id": 2, "period": "2024-весна", "current": 40, "final": 60},
        {"student_id": 2, "subject_id": 1, "period": "2024-весна", "current": 35, "final": 48},
        {"student_id": 2, "subject_id": 2, "period": "2024-весна", "current": 40, "final": 60},
    ]
    result = compare_periods(grades, SUBJECTS, "2023-осень", "2024-весна")
    assert result["period1"] == "2023-осень"
    assert result["period2"] == "2024-весна"
    assert result["absolute"]["trend"] == "рост"
    assert result["absolute"]["delta"] > 0
    assert result["weighted"]["trend"] == "рост"


def test_compare_periods_decline():
    grades = [
        {"student_id": 1, "subject_id": 1, "period": "2023-осень", "current": 40, "final": 60},
        {"student_id": 1, "subject_id": 1, "period": "2024-весна", "current": 30, "final": 30},
    ]
    result = compare_periods(grades, SUBJECTS, "2023-осень", "2024-весна")
    assert result["absolute"]["trend"] == "падение"
    assert result["absolute"]["delta"] < 0


def test_student_dynamics():
    grades = [
        {"student_id": 1, "subject_id": 1, "period": "2023-осень", "current": 35, "final": 40},
        {"student_id": 1, "subject_id": 1, "period": "2024-весна", "current": 38, "final": 55},
    ]
    result = student_dynamics(1, grades, SUBJECTS)
    assert len(result) == 2
    assert result[0]["period"] == "2023-осень"
    assert result[0]["absolute_rating"] == 75.0
    assert result[1]["period"] == "2024-весна"
    assert result[1]["absolute_rating"] == 93.0