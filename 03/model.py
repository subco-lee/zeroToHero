
class Task:
    def __init__(self,data:(int,str,str,bool)):
        self.id = data[0]
        self.title = data[1]
        self.content = data[2]
        self.done = data[3]

    def print_self(self):
        print(
            f'id: {self.id}\ntitle:{self.title}\ncontent:{self.content}\ndone:{self.done}')
