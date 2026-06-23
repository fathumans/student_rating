from app.storage.csv_exporter import export_rating_to_csv


def test_csv_export_format_combined():
    students = [
        {
            "absolute_rank": 1,
            "weighted_rank": 2,
            "name": "Гориченко М.С.",
            "group": "БИН-24-1",
            "absolute_rating": 100.0,
            "weighted_rating": 100.0,
            "rating_diff": -1,
            "excellent_count": 3,
        },
        {
            "absolute_rank": 2,
            "weighted_rank": 1,
            "name": "Анисимов Н.С.",
            "group": "БИН-24-1",
            "absolute_rating": 97.0,
            "weighted_rating": 97.31,
            "rating_diff": 1,
            "excellent_count": 2,
        },
    ]
    csv_text = export_rating_to_csv(students)
    lines = csv_text.strip().split("\r\n")

    assert len(lines) == 3  # BOM + заголовок + 2 студента
    assert "Место (абс)" in lines[0]
    assert "Место (взв)" in lines[0]
    assert "Гориченко" in lines[1]
    assert "Анисимов" in lines[2]
    assert "100,0" in lines[1] or "100.0" in lines[1]