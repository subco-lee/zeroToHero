from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from crud import create_task, delete_task, read_task, update_task
from models import Base
from schemas import TaskBase
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create", response_model=TaskBase)
def create_task_api(task: TaskBase, db: Session = Depends(get_db)):
    return create_task(db=db, task=task)

@app.post("/delete/{todo_id}")
def delete_task_api(todo_id: int, db: Session = Depends(get_db)):
    return delete_task(db=db, id_=todo_id)

@app.patch("/toggle/{todo_id}", response_model=TaskBase)
def update_task_api(todo_id: int, db: Session = Depends(get_db)):
    return update_task(db=db, id_=todo_id)

@app.get("/")
def read_root():
    return read_task(db=SessionLocal())
