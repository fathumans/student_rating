import csv
import io
from typing import List, Dict
from datetime import datetime


def export_rating_to_csv(students: List[Dict]) -> str:
    """
    Формирует CSV-строку с рейтингом.
    Используем ';' как разделитель — Excel на русской локали macOS/Windows
    открывает такой файл корректно (все столбцы на месте).
    BOM (\ufeff) заставляет Excel распознать UTF-8.
    """
    output = io.StringIO(newline='')
    writer = csv.writer(output, delimiter=';', lineterminator="\r\n")

    writer.writerow(["Место", "ФИО", "Рейтинг", "Дата экспорта"])

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    for s in students:
        writer.writerow([
            s.get("rank", ""),
            s.get("name", ""),
            s.get("rating", ""),
            now
        ])

    content = output.getvalue()
    return "\ufeff" + content


def export_rating_to_file(students: List[Dict], filepath: str) -> None:
    content = export_rating_to_csv(students)
    with open(filepath, "w", encoding="utf-8", newline='') as f:
        f.write(content)