from datetime import datetime, timedelta
import constansts


class Task:
    _task_amount = 0
    _task_scheduled_time = constansts.DEFAULT_SCHEDULED_TIME
    _task_priority = constansts.TASK_PRIORITIES['PRIORITY_3']

    def __new__(cls, *args, **kwargs):
        cls._task_amount += 1
        return super().__new__(cls)

    def __init__(self, title: str, value='', task_priority=None, scheduled_time=None):
        self._task_title = None
        self._task_value = None
        self.set_title(title)
        self.set_value(value)
        self.set_priority(task_priority)
        self.schedule_time(scheduled_time)
        self._task_id = self._task_amount
        self._task_creation_time = datetime.now()  # .strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def __validate_time(func):
        def wrapper(self, time, *args, **kwargs):
            if isinstance(time, datetime) and time >= datetime.now():
                func(self, time)
        return wrapper

    @staticmethod
    def __validate_text(func):
        def wrapper(self, text, *args, **kwargs):
            if len(str(text)) <= constansts.MAX_STRING_LEN:
                func(self, text)

        return wrapper

    @__validate_time
    def schedule_time(self, time: datetime):
        self._task_scheduled_time = time

    @__validate_text
    def set_value(self, value: str):
        self._task_value = str(value)

    @__validate_text
    def set_title(self, title: str):
        self._task_title = str(title)

    def set_priority(self, priority):
        if priority in constansts.TASK_PRIORITIES.values():
            self._task_priority = priority

    # def show_data(self):
    #     print(f'{self._task_priority}. {self._task_title} [{self._task_value}] запланировано на {self._task_scheduled_time}')

