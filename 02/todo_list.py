import time


class Task:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def printSelf(self):
        print(
            f'id: {self.id}\ntitle:{self.title}\ncontent:{self.content}')


def __main__():
    todos = []

    def add_todo(id, title, content):
        new_task = Task(id, title, content)
        todos.append(new_task)

    def get_todo_list():
        print("---Todos---")
        for todo in todos:
            todo.printSelf()
            print("\n")
        print("-----------")

    while (True):
        print("하고 싶은 일을 번호를 선택하세요!\n")
        print("1 - 할일 추가\n2 - 할일 조회하기")
        choice = int(input())
        if choice == 1:
            id = time.time()
            title = input("할 일의 제목을 입력해주세요: ")
            content = input("할 일의 내용을 입력해주세요: ")
            add_todo(id, title, content)
            print("할 일이 추가되었습니다!\n")

        elif choice == 2:
            get_todo_list()
        else:
            print("잘못된 입력값입니다.")


__main__()
