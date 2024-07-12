import datetime
import constansts
import validators


class Task:
    __task_amount = 0

    def __new__(cls, *args, **kwargs):
        cls.__task_amount += 1
        return super().__new__(cls)

    def __init__(self, title: str, value='', task_priority=constansts.TASK_PRIORITIES['PRIORITY_3'],
                 scheduled_time: datetime = constansts.DEFAULT_SCHEDULED_TIME):
        self.__task_title = self._task_value = self.__task_priority = self.__task_scheduled_time = None
        self.__task_id = self.__task_amount
        self.__task_creation_time = datetime.datetime.now()  # .strftime('%Y-%m-%d %H:%M:%S')
        self.set_title(title)
        self.set_value(value)
        self.set_priority(task_priority)
        self.schedule_time(scheduled_time)

    @validators.validate_time
    def schedule_time(self, time: datetime):
        self.__task_scheduled_time = time

    @validators.validate_text
    def set_value(self, value: str):
        self._task_value = str(value)

    @validators.validate_text
    def set_title(self, title: str):
        self.__task_title = str(title)

    def set_priority(self, priority):
        if priority in constansts.TASK_PRIORITIES.values():
            self.__task_priority = priority
        else:
            raise ValueError(f'incorrect priority key {priority},\
                             it should be one of {constansts.TASK_PRIORITIES.values()}')

    def get_data(self) -> (int, int, str, str, datetime, datetime):
        return self.__task_id, self.__task_priority, self.__task_title[0], self._task_value, \
               self.__task_creation_time, self.__task_scheduled_time
