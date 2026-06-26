import os
import shutil
import pytest
from fastapi.testclient import TestClient

os.environ["NO_SEED"] = "1"

from app.main import app
from app.storage import json_storage
from pathlib import Path
import tempfile

client = TestClient(app)

# Глобальные тестовые данные
TEST_STUDENTS = [
    {"id": 1, "name": "Анисимов Никита Сергеевич", "group": "БИН-24-1"},
    {"id": 2, "name": "Горин Даниил Витальевич", "group": "БИН-24-1"},
    {"id": 3, "name": "Гориченко Максим Сергеевич", "group": "БИН-24-1"},
    {"id": 4, "name": "Жуковец Даниил Денисович", "group": "БИН-24-1"},
    {"id": 5, "name": "Наконечный Кирилл Николаевич", "group": "БИН-24-1"},
]

TEST_SUBJECTS = [
    {"id": 1, "name": "Архитектура ЭВМ", "type": "exam", "weight": 1.0},
    {"id": 2, "name": "Иностранный язык в сфере ИТ", "type": "test", "weight": 0.6},
    {"id": 3, "name": "Исследование операций", "type": "exam", "weight": 1.0},
]

TEST_GRADES = [
    {"id": 1, "student_id": 1, "subject_id": 1, "period": "2026-весна", "current": 38, "final": 55},
    {"id": 2, "student_id": 1, "subject_id": 2, "period": "2026-весна", "current": 40, "final": 60},
    {"id": 3, "student_id": 1, "subject_id": 3, "period": "2026-весна", "current": 40, "final": 58},
    {"id": 4, "student_id": 2, "subject_id": 1, "period": "2026-весна", "current": 35, "final": 48},
    {"id": 5, "student_id": 2, "subject_id": 2, "period": "2026-весна", "current": 40, "final": 60},
    {"id": 6, "student_id": 2, "subject_id": 3, "period": "2026-весна", "current": 36, "final": 45},
    {"id": 7, "student_id": 3, "subject_id": 1, "period": "2026-весна", "current": 40, "final": 60},
    {"id": 8, "student_id": 3, "subject_id": 2, "period": "2026-весна", "current": 40, "final": 60},
    {"id": 9, "student_id": 3, "subject_id": 3, "period": "2026-весна", "current": 40, "final": 60},
    {"id": 10, "student_id": 4, "subject_id": 1, "period": "2026-весна", "current": 32, "final": 38},
    {"id": 11, "student_id": 4, "subject_id": 2, "period": "2026-весна", "current": 35, "final": 45},
    {"id": 12, "student_id": 4, "subject_id": 3, "period": "2026-весна", "current": 33, "final": 40},
    {"id": 13, "student_id": 5, "subject_id": 1, "period": "2026-весна", "current": 30, "final": 31},
    {"id": 14, "student_id": 5, "subject_id": 2, "period": "2026-весна", "current": 40, "final": 60},
    {"id": 15, "student_id": 5, "subject_id": 3, "period": "2026-весна", "current": 40, "final": 51},
]


# Session-scoped: бэкапим оригинальные данные один раз
@pytest.fixture(scope="session", autouse=True)
def backup_original_data():
    data_dir = json_storage.DATA_DIR
    backup_dir = Path(tempfile.mkdtemp())

    for fname in ["students.json", "subjects.json", "grades.json"]:
        src = data_dir / fname
        if src.exists():
            shutil.copy(str(src), str(backup_dir / fname))

    yield backup_dir

    # Восстанавливаем в конце сессии
    for fname in ["students.json", "subjects.json", "grades.json"]:
        src = backup_dir / fname
        dst = data_dir / fname
        if src.exists():
            shutil.copy(str(src), str(dst))
        elif dst.exists():
            dst.unlink()


@pytest.fixture(autouse=True)
def reset_test_data(backup_original_data):
    """Сбрасываем данные к тестовым перед каждым тестом."""
    json_storage.save_json("students.json", [s.copy() for s in TEST_STUDENTS])
    json_storage.save_json("subjects.json", [s.copy() for s in TEST_SUBJECTS])
    json_storage.save_json("grades.json", [g.copy() for g in TEST_GRADES])


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Рейтинговая система" in response.json()["message"]


def test_list_students():
    response = client.get("/api/students")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5
    assert data[3]["name"] == "Жуковец Даниил Денисович"


def test_create_student():
    response = client.post("/api/students", json={"name": "Тестовый Т.Т.", "group": "БИН-24-1"})
    assert response.status_code == 201
    assert response.json()["id"] == 6


def test_get_rating_combined():
    response = client.get("/api/rating")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5

    # Данные возвращаются в порядке students (по id), а не отсортированные
    # Находим конкретных студентов для проверки
    by_id = {s["id"]: s for s in data}

    # Гориченко (id=3) — отличник, 100 баллов
    gor = by_id[3]
    assert gor["absolute_rank"] == 1
    assert gor["absolute_rating"] == 100.0
    assert gor["weighted_rank"] == 1
    assert gor["weighted_rating"] == 100.0

    # Анисимов (id=1) — второй, 97 баллов
    ani = by_id[1]
    assert ani["absolute_rank"] == 2
    assert ani["absolute_rating"] == 97.0

    # Наконечный (id=5) — проверим детализацию
    nak = by_id[5]
    assert nak["absolute_rating"] == 84.0  # (61+100+91)/3 = 84? Проверь



def test_get_rating_absolute():
    response = client.get("/api/rating/absolute")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["absolute_rank"] == 1
    assert data[0]["name"] == "Гориченко Максим Сергеевич"
    assert "absolute_rating" in data[0]


def test_get_rating_weighted():
    response = client.get("/api/rating/weighted")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["weighted_rank"] == 1
    assert data[0]["name"] == "Гориченко Максим Сергеевич"
    assert "weighted_rating" in data[0]


def test_get_student_detail():
    response = client.get("/api/rating/student/5")
    assert response.status_code == 200
    data = response.json()
    assert data["student"]["name"] == "Наконечный Кирилл Николаевич"
    assert len(data["subjects"]) == 3
    assert data["subjects"][0]["total_score"] == 61
    assert data["subjects"][0]["grade"] == 3
    assert data["subjects"][0]["status"] == "Удовлетворительно"
    assert "absolute_rating" in data
    assert "weighted_rating" in data


def test_get_problem_subjects():
    response = client.get("/api/rating/problems?threshold=0.20")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_subjects_statistics():
    response = client.get("/api/rating/statistics")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert "average" in data[0]
    assert "std_dev" in data[0]


def test_export_csv():
    response = client.get("/api/rating/export")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]
    text = response.text
    assert "Место (абс)" in text
    assert "Гориченко" in text


def test_dynamics():
    response = client.get("/api/rating/dynamics?period1=2025-осень&period2=2026-весна")
    assert response.status_code == 200
    data = response.json()
    assert "absolute" in data
    assert "weighted" in data
    assert "trend" in data["absolute"]

def test_grade_validation_current_too_high():
    response = client.post("/api/grades", json={
        "student_id": 1,
        "subject_id": 1,
        "period": "2026-весна",
        "current": 45,
        "final": 50
    })
    assert response.status_code == 422

def test_create_and_enrich_grade():
    response = client.post("/api/grades", json={
        "student_id": 1,
        "subject_id": 1,
        "period": "2026-весна",
        "current": 35,
        "final": 50
    })
    assert response.status_code == 201
    data = response.json()
    assert data["total_score"] == 85
    assert data["grade"] == 4
    assert data["status"] == "Хорошо"


def test_grade_validation_final_too_high():
    response = client.post("/api/grades", json={
        "student_id": 1,
        "subject_id": 1,
        "period": "2026-весна",
        "current": 30,
        "final": 70
    })
    assert response.status_code == 422