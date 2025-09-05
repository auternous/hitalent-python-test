from fastapi import FastAPI
from app.routers import questions, answers

app = FastAPI()

app.include_router(questions)
app.include_router(answers)

@app.get("/")
def root():
    return {"message": "API работает. Перейдите на /docs для документации"}
