import json
import os
from typing import List, Dict, Any, Optional
from pathlib import Path


DATA_DIR = Path(os.getenv("DATA_DIR", "data"))


def _ensure_file(filename: str, default: Any = None) -> Path:
    """Создаёт файл с дефолтным значением, если его нет."""
    path = DATA_DIR / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        with open(path, "w", encoding="utf-8") as f:
            json.dump(default if default is not None else [], f, ensure_ascii=False, indent=2)
    return path


def load_json(filename: str) -> Any:
    """Загрузить содержимое JSON-файла."""
    path = _ensure_file(filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(filename: str, data: Any) -> None:
    """Атомарно сохранить данные в JSON."""
    path = _ensure_file(filename)
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(path)  # атомарная замена


# === Специфические операции для сущностей ===

def load_students() -> List[Dict]:
    return load_json("students.json")


def save_students(students: List[Dict]) -> None:
    save_json("students.json", students)


def load_subjects() -> List[Dict]:
    return load_json("subjects.json")


def save_subjects(subjects: List[Dict]) -> None:
    save_json("subjects.json", subjects)


def load_grades() -> List[Dict]:
    return load_json("grades.json")


def save_grades(grades: List[Dict]) -> None:
    save_json("grades.json", grades)


# === Универсальные CRUD-helpers ===

def get_next_id(items: List[Dict]) -> int:
    """Генерация следующего ID по максимальному существующему."""
    if not items:
        return 1
    return max(item.get("id", 0) for item in items) + 1


def add_item(filename: str, item: Dict, id_key: str = "id") -> Dict:
    """Добавить запись в файл, присвоить авто-ID."""
    data = load_json(filename)
    item[id_key] = get_next_id(data)
    data.append(item)
    save_json(filename, data)
    return item


def update_item(filename: str, item_id: int, updates: Dict, id_key: str = "id") -> Optional[Dict]:
    """Обновить запись по ID. Возвращает обновлённую запись или None."""
    data = load_json(filename)
    for entry in data:
        if entry.get(id_key) == item_id:
            entry.update(updates)
            # Не даём изменить ID
            entry[id_key] = item_id
            save_json(filename, data)
            return entry
    return None


def delete_item(filename: str, item_id: int, id_key: str = "id") -> bool:
    """Удалить запись по ID. Возвращает True если удалено."""
    data = load_json(filename)
    filtered = [entry for entry in data if entry.get(id_key) != item_id]
    if len(filtered) == len(data):
        return False
    save_json(filename, filtered)
    return True


def get_by_id(filename: str, item_id: int, id_key: str = "id") -> Optional[Dict]:
    """Найти запись по ID."""
    data = load_json(filename)
    for entry in data:
        if entry.get(id_key) == item_id:
            return entry
    return None