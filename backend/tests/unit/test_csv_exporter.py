from app.storage.csv_exporter import export_rating_to_csv


def test_csv_export_format():
    students = [
        {"rank": 1, "name": "Иванов И.И.", "rating": 4.8, "fives_count": 3},
        {"rank": 2, "name": "Петров П.П.", "rating": 4.2, "fives_count": 1},
    ]
    csv_text = export_rating_to_csv(students)
    lines = csv_text.strip().split("\n")

    assert len(lines) == 3  # заголовок + 2 студента
    assert lines[0] == "Место,ФИО,Рейтинг,Количество пятёрок,Дата экспорта"
    assert "Иванов" in lines[1]
    assert "Петров" in lines[2]