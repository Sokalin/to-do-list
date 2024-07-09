from datetime import datetime


class Task:
    _task_id = None
    _task_time = None
    _task_priority = None
    _task_value = None
    _task_amount = 0

    def __new__(cls, *args, **kwargs):
        Task._task_amount += 1
        return super().__new__(cls)

    def __init__(self, value=''):
        self._task_value = value
        self._task_id = self._task_amount
        self._task_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def show_data(self):
        print(f'{self._task_priority}. {self._task_value} [{self._task_id}/{self._task_amount}] - {self._task_time}')


class TaskPriority1(Task):
    _task_priority = 1


    # def __new__(cls, *args, **kwargs):
    #     cls._task_priority1_amount += 1
    #     return super().__new__(cls)




class TaskPriority2(Task):
    _task_priority = 2


class TaskPriority3(Task):
    _task_priority = 3
