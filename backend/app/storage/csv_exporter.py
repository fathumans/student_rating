import csv
import io
from typing import List, Dict
from datetime import datetime


def export_rating_to_csv(students: List[Dict]) -> str:
    """
    Экспорт объединённого рейтинга в CSV (Excel-friendly).
    """
    output = io.StringIO(newline='')
    writer = csv.writer(output, delimiter=';', lineterminator="\r\n")

    writer.writerow([
        "Место (абс)", "Место (взв)", "ФИО", "Группа",
        "Абсолютный балл", "Взвешенный балл", "Разница",
        "Отличных предметов", "Дата экспорта"
    ])

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    for s in students:
        writer.writerow([
            s.get("absolute_rank", ""),
            s.get("weighted_rank", ""),
            s.get("name", ""),
            s.get("group", ""),
            s.get("absolute_rating", ""),
            s.get("weighted_rating", ""),
            s.get("rating_diff", ""),
            s.get("excellent_count", ""),
            now
        ])

    return "\ufeff" + output.getvalue()


def export_student_detail_to_csv(student: Dict, subjects: List[Dict]) -> str:
    """Экспорт детализации студента в CSV."""
    output = io.StringIO(newline='')
    writer = csv.writer(output, delimiter=';', lineterminator="\r\n")

    writer.writerow(["Предмет", "Тип", "Вес", "Текущая (40)", "Промежуточная (60)", "Итог", "Оценка", "Статус"])
    for subj in subjects:
        writer.writerow([
            subj["subject_name"],
            subj["type"],
            subj["weight"],
            subj["current"],
            subj["final"],
            subj["total_score"],
            subj["grade"],
            subj["status"],
        ])

    writer.writerow([])
    writer.writerow(["Абсолютный рейтинг:", student.get("absolute_rating", "")])
    writer.writerow(["Взвешенный рейтинг:", student.get("weighted_rating", "")])

    return "\ufeff" + output.getvalue()