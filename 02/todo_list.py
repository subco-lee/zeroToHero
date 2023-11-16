import time


class Task:
    def __init__(self, id, title, content, done):
        self.id = id
        self.title = title
        self.content = content
        self.done = done

    def print_self(self):
        print(
            f'id: {self.id}\ntitle:{self.title}\ncontent:{self.content}\ndone:{self.done}')

    def toggle_done(self):
        self.done = not self.done
        if (self.done):
            print("완료로 변경되었습니다.\n")
        else:
            print("미완료로 변경되었습니다.\n")


def __main__():
    todos = {}

    def add_task(id, title, content):
        new_task = Task(id, title, content, False)
        todos[id] = new_task

    def get_todo_list():
        print("---------Todos---------")
        for value in todos.values():
            value.print_self()
            print("\n")
        print("-----------------------")

    def delete_task(id):
        del todos[id]

    def toggle_done(id):
        todos[id].toggle_done()

    while (True):
        print("하고 싶은 일을 번호를 선택하세요!\n")
        print("1 - 할일 추가\n2 - 할일 조회하기\n3 - 할일 삭제하기\n4 - 완료 상태 토글하기")
        choice = int(input())
        if choice == 1:
            id = str(time.time()).split(".")[0]
            title = input("할 일의 제목을 입력해주세요: ")
            content = input("할 일의 내용을 입력해주세요: ")
            add_task(id, title, content)

            print("할 일이 추가되었습니다!\n")

        elif choice == 2:
            get_todo_list()
        elif choice == 3:
            target_id = input("삭제할 할 일의 id 를 입력해주세요: ")
            delete_task(target_id)
        elif choice == 4:
            target_id = input("완료 상태를 토글할 할 일의 Id 를 입력해주세요: ")
            toggle_done(target_id)
        else:
            print("잘못된 입력값입니다.")


__main__()
