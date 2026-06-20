from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import students, subjects, grades, rating
from app.seed import seed_if_empty

app = FastAPI(
    title="Рейтинговая система студентов",
    description="Учебный проект Б-10. Алгоритмическое ядро: взвешенное агрегирование и ранжирование.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students.router, prefix="/api")
app.include_router(subjects.router, prefix="/api")
app.include_router(grades.router, prefix="/api")
app.include_router(rating.router, prefix="/api")


@app.on_event("startup")
def startup():
    seed_if_empty()


@app.get("/")
def root():
    return {
        "message": "Рейтинговая система студентов",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {"status": "ok"} 