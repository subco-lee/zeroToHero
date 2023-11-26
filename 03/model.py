
class Task:
    def __init__(self, id: int, title: str, content: str, done: bool):
        self.id = id
        self.title = title
        self.content = content
        self.done = done

    def __str__(self):
        return (f'id: {self.id}\ntitle:{self.title}\ncontent:{self.content}\ndone:{self.done}')
