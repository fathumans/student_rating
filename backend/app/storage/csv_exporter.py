import csv
import io
from typing import List, Dict
from datetime import datetime


def export_rating_to_csv(students: List[Dict]) -> str:
    """
    Формирует CSV-строку с рейтингом.
    students: список, полученный из ranker (с полями rank, name, rating, fives_count)
    """
    output = io.StringIO()
    writer = csv.writer(output, lineterminator="\n")

    # Заголовок
    writer.writerow(["Место", "ФИО", "Рейтинг", "Количество пятёрок", "Дата экспорта"])

    # Данные
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    for s in students:
        writer.writerow([
            s.get("rank", ""),
            s.get("name", ""),
            s.get("rating", ""),
            s.get("fives_count", ""),
            now
        ])

    return output.getvalue()


def export_rating_to_file(students: List[Dict], filepath: str) -> None:
    """Сохранить CSV на диск."""
    content = export_rating_to_csv(students)
    with open(filepath, "w", encoding="utf-8-sig") as f:
        f.write(content)