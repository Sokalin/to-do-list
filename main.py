import data_models
import datetime
from database import DataBaseManager


if __name__ == '__main__':
    with DataBaseManager('tasks.db') as DataBase:
        DataBase.delete_all_tables()
        DataBase.get_info()
        DataBase.create_table('jkjkj', {'id': 'INTEGER', 'name': 'TEXT', 'surname': 'TEXT'})
        DataBase.get_info()
        DataBase.add_record('jkjkj', [1, 'jhon', 'doe'])
    # database.db_create()
    a1 = data_models.Task('Попиjkljjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjsdffть кофе', 'токо не растворимый', 1)

    # a2 = data_models.Task('Спать')

    # a3 = data_models.Task('Писать код', 'написать дазу данных и класс для ее управления', 2)
    # a3.schedule_time(datetime.datetime(2025, 7, 20))
    # print(a3.__task_scheduled_time)
    # database.db_update(a1.get_data())
    # database.db_update(a2.get_data())
    # a2.set_title('Sleep')


