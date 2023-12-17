from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from crud import create_task, delete_task, read_task, update_task
from models import Base
from schemas import TaskBase, TaskCreate
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/task", response_model=TaskBase)
def create_task_api(task: TaskBase, db: Session = Depends(get_db)):
    return create_task(db=db, task=task)


@app.get("/")
def read_root():
    return read_task(db=SessionLocal())

@app.post("/sum")
def sum(a: int, b: int):
    # if not isinstance(a, int) or not isinstance(b, int):
    #     raise HTTPException(status_code=422, detail="[ERROR] a and b must be int")
    return {"sum": a + b}