from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(
    prefix="/answers",
    tags=["answers"],
)

@router.post("/questions/{question_id}/answers/", response_model=schemas.Answer)
def create_answer(question_id: int, answer: schemas.AnswerCreate, db: Session = Depends(get_db)):
    question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    if not answer.text or answer.text.strip() == "":
        raise HTTPException(status_code=400, detail="Answer text cannot be empty")
    db_answer = models.Answer(question_id=question_id, user_id=answer.user_id, text=answer.text)
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

@router.get("/{id}", response_model=schemas.Answer)
def get_answer(id: int, db: Session = Depends(get_db)):
    answer = db.query(models.Answer).filter(models.Answer.id == id).first()
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_answer(id: int, db: Session = Depends(get_db)):
    answer = db.query(models.Answer).filter(models.Answer.id == id).first()
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    db.delete(answer)
    db.commit()
