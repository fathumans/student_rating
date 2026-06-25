Рейтинговая система студентов — учебная ознакомительная практика 2026

Студент: Наконечный Кирилл Николаевич
Группа: БИН-24-1
Вариант: Б-10 — Рейтинговая система студентов
Язык: Python 3.12

Описание

Веб-приложение для учёта оценок по предметам для группы студентов. Алгоритмическое ядро реализует взвешенное агрегирование оценок (текущая 40% + промежуточная 60%) и ранжирование студентов по абсолютному и взвешенному рейтингу. Функционал включает динамику успеваемости по периодам, сравнение студентов, выявление проблемных предметов и экспорт рейтинга в CSV.

Структура репозитория

.
├── backend/
│   ├── app/
│   │   ├── main.py              # точка входа FastAPI
│   │   ├── routers/             # API-эндпоинты (students, subjects, grades, rating)
│   │   ├── core/                # алгоритмическое ядро (ranker, aggregator, analyzer, converter, dynamics)
│   │   ├── storage/             # работа с JSON-файлами (CRUD)
│   │   └── schemas.py           # Pydantic-модели
│   ├── data/                    # файлы данных (JSON)
│   ├── tests/
│   │   ├── unit/                # юнит-тесты алгоритмического ядра
│   │   ├── integration/         # интеграционные тесты API
│   │   └── fixtures/            # тестовые данные
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── App.jsx              # корневой компонент
│   │   ├── components/          # React-компоненты (RatingView, AnalyticsView, GradeManager, StudentManager, SubjectManager)
│   │   └── api/client.js        # HTTP-клиент для API
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml           # оркестрация backend + frontend
├── README.md
└── .gitignore

Установка и запуск

Локально (без Docker)

# 1. Клонировать репозиторий
git clone https://github.com/&lt;username&gt;/student_rating.git
cd student_rating

# 2. Бэкенд
cd backend
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt

# 3. Запуск бэкенда (из папки backend)
uvicorn app.main:app --reload --port 8000

# 4. Фронтенд (в новом терминале)
cd frontend
npm install
npm run dev

# 5. Открыть в браузере
# Фронтенд: http://localhost:5173
# API:      http://localhost:8000
# Документация API: http://localhost:8000/docs

В Docker

# Собрать и запустить всё
docker-compose up --build

# Открыть в браузере
# Фронтенд: http://localhost
# API:      http://localhost:8000
# Документация API: http://localhost:8000/docs

# Остановить
docker-compose down

Запуск тестов

# Юнит-тесты
cd backend
pytest tests/unit/ -v

# Интеграционные тесты
pytest tests/integration/ -v

# Все тесты
pytest tests/ -v

Зависимости

Бэкенд
- Python ≥ 3.12
- fastapi 0.111.0
- uvicorn[standard] 0.30.0
- pydantic 2.7.0
- pytest 8.2.0
- httpx 0.27.0

Фронтенд
- Node.js ≥ 20
- React 19.2.6
- Vite 8.0.12
- Bootstrap 5.3.8
- Recharts 3.9.0

Основные функции

| Функция | Описание |
|---------|----------|
| Управление студентами | Добавление, удаление, фильтрация по группам |
| Управление предметами | Зачёты, практики, экзамены с весами |
| Учёт оценок | Текущая (40) + промежуточная (60) = итог (100) |
| Рейтинг | Абсолютный и взвешенный рейтинг с ранжированием |
| Аналитика | Распределение, профиль студента, сравнение, проблемные предметы, динамика |
| Экспорт | CSV с фильтрацией по группе |
| Группы | Общий выбор группы для всех вкладок |

Алгоритмическое ядро

- **Агрегирование**: суммирование баллов с учётом весов предметов
- **Ранжирование**: сортировка по абсолютному и взвешенному рейтингу
- **Конвертация**: перевод баллов в оценки (отлично/хорошо/удовл/неуд) и статусы (зачёт/незачёт)
- **Анализ**: выявление проблемных предметов (средний балл &lt; 75) и динамика по периодам
- **Экспорт**: формирование CSV с BOM для корректного открытия в Excel

Данные

Все данные хранятся в JSON-файлах (`backend/data/`):
- `students.json` — список студентов
- `subjects.json` — список предметов с весами
- `grades.json` — оценки по периодам

СУБД не используется (требование варианта).