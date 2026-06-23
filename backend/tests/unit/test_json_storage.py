import json
import os
import tempfile
import pytest
from pathlib import Path

from app.storage import json_storage


@pytest.fixture
def temp_data_dir():
    """Временная папка для данных, изолированная от реальных файлов."""
    with tempfile.TemporaryDirectory() as tmp:
        old_dir = json_storage.DATA_DIR
        json_storage.DATA_DIR = Path(tmp)
        yield tmp
        json_storage.DATA_DIR = old_dir


def test_load_empty_file(temp_data_dir):
    data = json_storage.load_json("empty.json")
    assert data == []


def test_save_and_load(temp_data_dir):
    payload = [{"id": 1, "name": "Test"}]
    json_storage.save_json("test.json", payload)
    loaded = json_storage.load_json("test.json")
    assert loaded == payload


def test_add_item(temp_data_dir):
    item = {"name": "Иванов"}
    result = json_storage.add_item("students.json", item)
    assert result["id"] == 1
    assert result["name"] == "Иванов"

    second = json_storage.add_item("students.json", {"name": "Петров"})
    assert second["id"] == 2


def test_update_item(temp_data_dir):
    json_storage.add_item("students.json", {"name": "Иванов"})
    updated = json_storage.update_item("students.json", 1, {"name": "Сидоров"})
    assert updated is not None
    assert updated["name"] == "Сидоров"
    assert updated["id"] == 1


def test_update_nonexistent(temp_data_dir):
    assert json_storage.update_item("students.json", 99, {"name": "X"}) is None


def test_delete_item(temp_data_dir):
    json_storage.add_item("students.json", {"name": "Иванов"})
    assert json_storage.delete_item("students.json", 1) is True
    assert json_storage.load_json("students.json") == []


def test_delete_nonexistent(temp_data_dir):
    assert json_storage.delete_item("students.json", 99) is False


def test_get_by_id(temp_data_dir):
    json_storage.add_item("students.json", {"name": "Иванов"})
    found = json_storage.get_by_id("students.json", 1)
    assert found["name"] == "Иванов"
    assert json_storage.get_by_id("students.json", 99) is None


def test_specific_loaders(temp_data_dir):
    fixtures = Path(__file__).parent.parent / "fixtures"
    for fname in ["students.json", "subjects.json", "grades.json"]:
        src = fixtures / fname
        if src.exists():
            dst = Path(temp_data_dir) / fname
            dst.write_text(src.read_text(), encoding="utf-8")

    students = json_storage.load_students()
    assert len(students) == 5  # теперь 5 студентов в фикстурах
    assert students[0]["name"] == "Анисимов Никита Сергеевич"

    subjects = json_storage.load_subjects()
    assert subjects[0]["weight"] == 1.0