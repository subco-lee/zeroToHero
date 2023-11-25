from model import Task
import sqlite3

MY_TODO_TABLE = 'TODO_LIST'


def create_db():
    con = sqlite3.connect('./todos.db')
    return con


def init_db(con: sqlite3.Connection):
    cursor = con.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {MY_TODO_TABLE} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            done BOOLEAN
        )''')
    cursor.close()



def create_task(con: sqlite3.Connection, title: str, content: str):
    cursor = con.cursor()
    cursor.execute(f'''
        INSERT INTO {MY_TODO_TABLE} (title, content, done)
        VALUES ('{title}', '{content}', {False})
    ''')
    cursor.close()
    con.commit()


def read_task(con: sqlite3.Connection):
    cursor = con.cursor()
    cursor.execute(f'''
        SELECT * FROM {MY_TODO_TABLE}
    ''')
    todos = cursor.fetchall()
    cursor.close()
    tasks = [Task(todo) for todo in todos]
    return tasks


def update_task(con: sqlite3.Connection, _id: int):
    cursor = con.cursor()
    cursor.execute(f'''
        SELECT * FROM {MY_TODO_TABLE}
        WHERE id = {_id}
    ''')
    todo = cursor.fetchone()

    if todo is None:
        print("잘못된 id 입니다.")
        return
    else:
        task = Task(todo)
        new_done_status = True if task.done == False else False
        cursor.execute(f'''
            UPDATE {MY_TODO_TABLE}
            SET done = {new_done_status}
            WHERE id = {_id}
        ''')
    cursor.close()
    con.commit()


def delete_task(con: sqlite3.Connection, _id: int):
    cursor = con.cursor()
    cursor.execute(f'''
        DELETE FROM {MY_TODO_TABLE}
        WHERE id = {_id}
    ''')
    cursor.close()
    con.commit()
