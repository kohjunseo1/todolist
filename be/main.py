from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import model

model.Base.metadata.create_all(bind=engine)


class Todolist_DTO(BaseModel):
    id: int
    subject: str
    content: str


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/")
def read_root():
    # example = session.query(Todolist).all()
    return "example"


@app.get("/todolist/{todolist_id}")
def get_todolist(todolist_id):
    return f"todolist_id = {todolist_id}"


@app.post("/todolist")
async def create_todolist(
    id: int, subject: str, content: str, db: Session = Depends(get_db)
):
    new_todolist = model.Todolist(
        id=int(id),
        subject=str(subject),
        content=str(content),
    )
    db.add(new_todolist)
    db.commit()
    db.refresh(new_todolist)
    return {"new_todolist": new_todolist}
