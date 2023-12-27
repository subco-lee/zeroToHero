from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    content: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    id: int

class TaskDelete(BaseModel):
    id: int