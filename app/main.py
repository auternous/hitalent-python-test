from fastapi import FastAPI
from app.routers import questions, answers

app = FastAPI()

app.include_router(questions)
app.include_router(answers)
