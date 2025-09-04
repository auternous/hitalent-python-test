# Запуск проекта Q&A API

Этот документ описывает, как быстро запустить проект с вопросами и ответами на FastAPI с PostgreSQL и Docker.

![Demo](assets/demo.gif)
---

## Клонирование репозитория

```
git clone [<URL_репозитория>](https://github.com/auternous/hitelent-python-test.git)
cd hitelent-python-test
```

---

## Запуск через Docker Compose

```
docker-compose up --build
```

- Запустятся контейнеры с базой данных PostgreSQL и веб-приложением.
- После запуска API будет доступен по адресу: http://localhost:8000  
- Документация Swagger UI: http://localhost:8000/docs

---

## Основные команды для Alembic миграций

Создать новую миграцию:

```
docker-compose run --rm web alembic revision --autogenerate -m "описание изменений"
```

Применить миграции:

```
docker-compose run --rm web alembic upgrade head
```

---

## Примеры API-запросов

Получить все вопросы:

```
GET /questions/
```

Создать вопрос:

```
POST /questions/
Content-Type: application/json

{
  "text": "Ваш вопрос"
}
```

Добавить ответ к вопросу:

```
POST /answers/questions/{question_id}/answers/
Content-Type: application/json

{
  "user_id": "user123",
  "text": "Текст ответа"
}
```

---

## Тестирование

Запуск тестов:

```
pytest tests/ -v
```

В Docker:

```
docker-compose exec web pytest tests/ -v
```

---

## Остановка проекта

```
docker-compose down -v
```

---

## Структура проекта

```
app/
├── main.py
├── models.py
├── schemas.py
├── database.py
└── routers/
    ├── questions.py
    └── answers.py

alembic/
tests/
Dockerfile
docker-compose.yml
requirements.txt
README.md
.gitignore
```

