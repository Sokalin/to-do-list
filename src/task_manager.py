from src import database
from src import data_models
from src import constansts
import datetime


class TaskManager:
    def __init__(self):
        self.__file = 'tasks.db'
        self.__task_table_name = 'tasks'
        self.__database = database.DataBaseManager(self.__file)
        with self.__database as db:
            db.delete_all_tables()
            db.create_table(self.__task_table_name, {'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                                                     'priority': 'INTEGER',
                                                     'title': 'TEXT',
                                                     'value': 'TEXT',
                                                     'creation_time': 'FLOAT',
                                                     'scheduled_time': 'FLOAT'})

    def create_task(self, title: str, value='', task_priority=constansts.TASK_PRIORITIES['PRIORITY_3'],
                    scheduled_time=constansts.DEFAULT_SCHEDULED_TIME):
        with self.__database as db:
            db.add_record(self.__task_table_name,
                          data_models.Task(title, value, task_priority, scheduled_time).get_data())

    def create_repetitive_task(self):
        pass

    def del_task(self, condition):
        with self.__database as db:
            db.delete_record(self.__task_table_name, condition)

    def update_task(self, updated_values: dict, condition):
        with self.__database as db:
            db.update_record(self.__task_table_name,updated_values, condition)

    def get_all_tasks(self) -> list:
        with self.__database as db:
            return db.get_records_by_condition(self.__task_table_name)

    def get_today_tasks(self):
        with self.__database as db:
            return db.get_records_by_condition(self.__task_table_name,
                                               f'scheduled_time < {datetime.datetime.timestamp(datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day) + datetime.timedelta(days=1))}')

    def get_week_task(self):
        with self.__database as db:
            return db.get_records_by_condition(self.__task_table_name,
                                               f'scheduled_time < {datetime.datetime.timestamp(datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day) + datetime.timedelta(days=7))}')

    def get_repetitive_tasks(self):
        pass
