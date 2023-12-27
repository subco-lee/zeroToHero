from sqlalchemy import Boolean, Column, Integer, String

from database import Base

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=False)
    content = Column(String, index=False)
    done = Column(Boolean, index=False)

    def __str__(self):
        return (f'id: {self.id}\ntitle:{self.title}\ncontent:{self.content}\ndone:{self.done}')
