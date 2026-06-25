import csv
import io
from typing import List, Dict


def export_rating_to_csv(students: List[Dict]) -> str:
    output = io.StringIO(newline='')
    writer = csv.writer(output, delimiter=';', lineterminator="\r\n")

    writer.writerow([
        "Место (абс)", "Место (взв)", "ФИО", "Группа",
        "Абсолютный балл", "Взвешенный балл"
    ])

    for s in students:
        writer.writerow([
            s.get("absolute_rank", ""),
            s.get("weighted_rank", ""),
            s.get("name", ""),
            s.get("group", ""),
            s.get("absolute_rating", ""),
            s.get("weighted_rating", ""),
        ])

    return "\ufeff" + output.getvalue()