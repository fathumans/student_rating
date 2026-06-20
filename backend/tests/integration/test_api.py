import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.storage import json_storage
from pathlib import Path
import tempfile
import shutil

client = TestClient(app)


@pytest.fixture(autouse=True)
def isolate_data():
    """Изолируем тесты от реальных данных."""
    with tempfile.TemporaryDirectory() as tmp:
        old_dir = json_storage.DATA_DIR
        json_storage.DATA_DIR = Path(tmp)
        # Копируем фикстуры
        fixtures = Path(__file__).parent.parent / "fixtures"
        for fname in ["students.json", "subjects.json", "grades.json"]:
            src = fixtures / fname
            if src.exists():
                shutil.copy(src, Path(tmp) / fname)
        yield
        json_storage.DATA_DIR = old_dir


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Рейтинговая система" in response.json()["message"]


def test_list_students():
    response = client.get("/students")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert data[0]["name"] == "Иванов Иван Иванович"


def test_create_student():
    response = client.post("/students", json={"name": "Кузнецов К.К.", "group": "БИН-24-1"})
    assert response.status_code == 201
    assert response.json()["id"] == 4


def test_get_rating():
    response = client.get("/rating")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert data[0]["rank"] == 1
    assert "rating" in data[0]


def test_get_problem_subjects():
    response = client.get("/rating/problems?threshold=0.15")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_export_csv():
    response = client.get("/rating/export")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]
    text = response.text
    assert "Место" in text
    assert "Иванов" in text


def test_dynamics():
    response = client.get("/rating/dynamics?period1=2024-осень&period2=2024-весна")
    assert response.status_code == 200
    data = response.json()
    assert "trend" in data


def test_crud_subject():
    # Создание
    r = client.post("/subjects", json={"name": "История", "type": "test", "weight": 0.2})
    assert r.status_code == 201
    sid = r.json()["id"]
    # Получение
    r = client.get(f"/subjects/{sid}")
    assert r.status_code == 200
    assert r.json()["name"] == "История"
    # Удаление
    r = client.delete(f"/subjects/{sid}")
    assert r.status_code == 204