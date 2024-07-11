import data_models
import datetime
from database import DataBase


if __name__ == '__main__':
    datbas = DataBase('tasks.db')
    datbas.create_table('jkjkj')

    # database.db_create()
    a1 = data_models.Task('Попить кофе', 'токо не растворимый', 1)

    # a2 = data_models.Task('Спать')

    # a3 = data_models.Task('Писать код', 'написать дазу данных и класс для ее управления', 2)
    # a3.schedule_time(datetime.datetime(2025, 7, 20))
    # print(a3._task_scheduled_time)
    # database.db_update(a1.get_data())
    # database.db_update(a2.get_data())
    # a2.set_title('Sleep')


