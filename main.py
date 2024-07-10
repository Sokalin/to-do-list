import data_models
import datetime


if __name__ == '__main__':
    a1 = data_models.Task('Попить кофе', 'токо не растворимый', 1)
    a1.show_data()
    a2 = data_models.Task('Спать')
    a2.show_data()
    a3 = data_models.Task('Писать код', 'написать дазу данных и класс для ее управления', 2)
    a3.show_data()
    a3.schedule_time(datetime.datetime(2024, 7, 20, 18))
    TASK_PRIORITIES = {'TASK_PRIORITY_1': 1, 'TASK_PRIORITY_2': 2, 'TASK_PRIORITY_3': 3}
    print(TASK_PRIORITIES['TASK_PRIORITY_3'])
    for a in [a1, a2, a3]:

        a.show_data()

