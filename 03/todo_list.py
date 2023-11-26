from db import create_db, init_db, delete_task, create_task, read_task, update_task


def todo_list():
    con = create_db()
    init_db(con)
    def add_task():
        title = input("할 일의 제목을 입력해주세요: ")
        content = input("할 일의 내용을 입력해주세요: ")
        create_task(con, title, content)

        print("할 일이 추가되었습니다!\n")

    def get_todo_list():
        todos = read_task(con)
        print("---------Todos---------")
        for todo in todos:
            print(todo)
        print("-----------------------")

    def delete_my_task():
        target_id = input("삭제할 할 일의 id 를 입력해주세요: ")
        delete_task(con, target_id)

    def toggle_done():
        target_id = input("완료 상태를 토글할 할 일의 Id 를 입력해주세요: ")
        update_task(con, target_id)

    NUMBER_TO_FUNCTION = {
        1: add_task,
        2: get_todo_list,
        3: delete_my_task,
        4: toggle_done
    }

    while True:
        print("하고 싶은 일을 번호를 선택하세요!\n")
        print("1 - 할일 추가\n2 - 할일 조회하기\n3 - 할일 삭제하기\n4 - 완료 상태 토글하기")
        choice = int(input())

        if choice not in NUMBER_TO_FUNCTION:
            print("잘못된 입력입니다. 다시 입력해주세요.")
        else:
            NUMBER_TO_FUNCTION[choice]()
        

if __name__ == "__main__":
    todo_list()