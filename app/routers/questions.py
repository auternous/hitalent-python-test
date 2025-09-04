from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from typing import List

router = APIRouter(
    prefix="/questions",
    tags=["questions"],
)

@router.get("/", response_model=List[schemas.Question])
def get_questions(db: Session = Depends(get_db)):
    return db.query(models.Question).all()

@router.post("/", response_model=schemas.Question)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    if not question.text or question.text.strip() == "":
        raise HTTPException(status_code=400, detail="Question text cannot be empty")
    db_question = models.Question(text=question.text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

@router.get("/{id}", response_model=schemas.Question)
def get_question(id: int, db: Session = Depends(get_db)):
    question = db.query(models.Question).filter(models.Question.id == id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(id: int, db: Session = Depends(get_db)):
    question = db.query(models.Question).filter(models.Question.id == id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    db.delete(question)
    db.commit()
