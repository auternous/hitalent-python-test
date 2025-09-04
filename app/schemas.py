from pydantic import BaseModel
from datetime import datetime
from typing import List

class AnswerBase(BaseModel):
    user_id: str
    text: str

class AnswerCreate(AnswerBase): pass

class Answer(AnswerBase):
    id: int
    question_id: int
    created_at: datetime
    class Config:
        orm_mode = True

class QuestionBase(BaseModel):
    text: str

class QuestionCreate(QuestionBase): pass

class Question(QuestionBase):
    id: int
    created_at: datetime
    answers: List[Answer] = []
    class Config:
        orm_mode = True
