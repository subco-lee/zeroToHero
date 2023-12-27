from sqlalchemy.orm import Session
from uuid import uuid4

from models import Task
from schemas import TaskCreate

def create_task(db: Session, task: TaskCreate):
    db_task = Task(title=task.title, content=task.content, done=False)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def read_task(db: Session, limit: int = 100):
    return db.query(Task).limit(limit).all()

def update_task(db: Session, id_: int):
    db_task = db.query(Task).filter(Task.id == id_).first()
    if db_task is None:
        print("[ERROR]: 잘못된 id 입니다.")
        return
    else:
        db_task.done = not db_task.done
        db.commit()
        db.refresh(db_task)
        return db_task
    
def delete_task(db: Session, id_: int):
    db_task = db.query(Task).filter(Task.id == id_).first()
    if db_task is None:
        print("[ERROR]: 잘못된 id 입니다.")
        return
    else:
        db.delete(db_task)
        db.commit()
        return db_task
