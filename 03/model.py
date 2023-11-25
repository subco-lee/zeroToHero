
class Task:
    def __init__(self, _id, title, content, done):
        self.id = _id
        self.title = title
        self.content = content
        self.done = done

    def print_self(self):
        print(
            f'id: {self.id}\ntitle:{self.title}\ncontent:{self.content}\ndone:{self.done}')
