import sqlite3
import constansts


class DataBase:
    def __init__(self, file: str):
        self.__file = file

    def create_table(self, name: str, **values):
        with sqlite3.connect(self.__file) as bd:
            cur = bd.cursor()

            for key in values.keys():
                if key not in constansts.SQLITE3_DATA_TYPES:
                    raise ValueError('неверный тип данных')

            cur.execute(f'''CREATE TABLE IF NOT EXISTS {name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            priority INTEGER,
            itle TEXT,
            value TEXT)''')

    def delete_table(self, name: str):
        with sqlite3.connect(self.__file) as bd:
            cur = bd.cursor()
            cur.execute(f'DROP TABLE IF EXISTS {name}')

    def add_record(self, table_name):
        pass

    def update_record(self, table_name):
        pass


def db_delete():
    with sqlite3.connect("tasks.db") as all_tasks:
        cur = all_tasks.cursor()

        cur.execute('''DROP TABLE IF EXISTS all_tasks''')


def db_create():
    with sqlite3.connect("tasks.db") as all_tasks:
        cur = all_tasks.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS all_tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                priority INTEGER,
                title TEXT,
                value TEXT,
                creation_time TEXT,
                scheduled_time TEXT
                )''')


def delete_row(row_id):
    with sqlite3.connect("tasks.db") as all_tasks:
        cur = all_tasks.cursor()

        cur.execute('DELETE FROM all_tasks WHERE id = ?', (row_id,))


def add_new_row(val):
    with sqlite3.connect("tasks.db") as all_tasks:
        cur = all_tasks.cursor()

        # cur.execute('INSERT INTO all_tasks (id, priority) VALUES (1, 1)')
        cur.execute(f'INSERT INTO all_tasks VALUES (?, ?, ?, ?, ?, ?)', val)

        # cur.execute(''''DROP TABLE users''') для удаления таблицы (в настр функция сохранения и сброса)
