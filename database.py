import sqlite3
import validators


class DataBaseManager:
    def __init__(self, file: str):
        self.__db_file = file

    def __enter__(self):
        self.__connection = sqlite3.connect(self.__db_file)
        self.__cursor = self.__connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__connection.commit()
        self.__connection.close()

    def create_table(self, table_name: str, columns: dict):
        """
        Создает таблицу с заданным именем и колонками.
        :param table_name: str, имя таблицы
        :param columns: dict, словарь с именами колонок и их типами данных (например, {"id": "INTEGER PRIMARY KEY", "name": "TEXT"})
        """
        columns_def = ", ".join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
        table_creation_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})"
        self.__cursor.execute(table_creation_query)

    def delete_table(self, table_name: str):
        self.__cursor.execute(f'DROP TABLE IF EXISTS {table_name}')

    def delete_all_tables(self):
        for table in self.__cursor.execute('SELECT * FROM SQLITE_SCHEMA WHERE type=\'table\''):
            if table[1] != 'sqlite_sequence':
                self.__cursor.execute(f'DROP TABLE IF EXISTS {table[1]}')

    def add_record(self, table_name: str, values):

        self.__cursor.execute(f'SELECT * FROM {table_name}')
        columns = tuple(column[0] for column in self.__cursor.description)

        for table in self.__cursor.execute('SELECT * FROM SQLITE_SCHEMA WHERE type=\'table\''):
            if table[1] == table_name and len(values) == len(columns):
                self.__cursor.execute(f'INSERT INTO {table_name} {columns} VALUES {tuple(values)}')
                return None
        raise ValueError(f'Таблицы {table_name} не существует или неверные данные')

    def update_record(self, table_name):
        pass

    def backup_table(self):
        pass

    def get_info(self):
        print(f'{self.__db_file}: {[x for x in self.__cursor.execute("SELECT * FROM SQLITE_SCHEMA")]}')
