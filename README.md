# Рейтинговая система студентов — учебная ознакомительная практика 2026

**Студент:** Наконечный Кирилл Николаевич  
**Группа:** БИН-24-1  
**Вариант:** Б-10 — *Рейтинговая система студентов*  
**Язык:** Python 3.12

## Описание

Веб-приложение для учёта оценок по предметам для группы студентов. Алгоритмическое ядро реализует взвешенное агрегирование оценок (текущая 40% + промежуточная 60%) и ранжирование студентов по абсолютному и взвешенному рейтингу.

## Структура репозитория

```
.
├── backend/
│   ├── app/
│   │   ├── main.py              # точка входа FastAPI
│   │   ├── routers/             # API-эндпоинты
│   │   ├── core/                # алгоритмическое ядро
│   │   ├── storage/             # работа с JSON-файлами
│   │   └── schemas.py           # Pydantic-модели
│   ├── data/
│   │   ├── students.json        # список студентов
│   │   ├── subjects.json        # список предметов
│   │   └── grades.json          # оценки по периодам
│   ├── tests/
│   │   ├── unit/                # юнит-тесты алгоритма
│   │   ├── integration/         # интеграционные тесты API
│   │   └── fixtures/            # тестовые данные
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── App.jsx              # корневой компонент
│   │   ├── components/          # React-компоненты
│   │   └── api/client.js        # HTTP-клиент
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Установка и запуск

### Локально

```bash
# 1. Клонировать репозиторий
git clone https://github.com/<username>/student_rating.git
cd student_rating

# 2. Бэкенд
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Запуск бэкенда (из папки backend)
uvicorn app.main:app --reload --port 8000

# 4. Фронтенд (в новом терминале)
cd frontend
npm install
npm run dev
```

### В Docker

```bash
# Собрать и запустить всё
docker-compose up --build

# Остановить
docker-compose down
```

## Параметры запуска

| Параметр | Описание | По умолчанию |
|----------|----------|--------------|
| `--input` | Путь к файлу с входными данными | `backend/data/` |
| `--output` | Путь к файлу результата | stdout |
| `--verbose` | Подробный вывод | выключен |

## Запуск тестов

```bash
# Все тесты
cd backend
pytest tests/ -v

# Юнит-тесты
pytest tests/unit/ -v

# Интеграционные тесты
pytest tests/integration/ -v
```

## Зависимости

- Python ≥ 3.12
- fastapi 0.111.0
- uvicorn[standard] 0.30.0
- pydantic 2.7.0
- pytest 8.2.0
- httpx 0.27.0
- Node.js ≥ 20
- React 19.2.6
- Vite 8.0.12
- Bootstrap 5.3.8
- Recharts 3.9.0