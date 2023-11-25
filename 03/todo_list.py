from db import create_db, init_db, delete_task, create_task, read_task, update_task


def __main__():
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
            todo.print_self()
            print("\n")
        print("-----------------------")

    def delete_my_task():
        target_id = input("삭제할 할 일의 id 를 입력해주세요: ")
        delete_task(con, target_id)

    def toggle_done():
        target_id = input("완료 상태를 토글할 할 일의 Id 를 입력해주세요: ")
        update_task(con, target_id)

    while True:
        print("하고 싶은 일을 번호를 선택하세요!\n")
        print("1 - 할일 추가\n2 - 할일 조회하기\n3 - 할일 삭제하기\n4 - 완료 상태 토글하기")
        choice = int(input())
        if choice == 1:
            add_task()
        elif choice == 2:
            get_todo_list()
        elif choice == 3:
            delete_my_task()
        elif choice == 4:
            toggle_done()
        else:
            print("잘못된 입력값입니다.")


__main__()
