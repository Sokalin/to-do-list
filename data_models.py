import datetime
import constansts
import validators


def get_timestamp_from_date(year, month, day, hour=0, minute=0, second=0):
    validators.validate_time_data(year, month, day, hour, minute, second)
    return datetime.datetime.timestamp(datetime.datetime(year, month, day, hour, minute, second))


def get_date_from_timestamp(timestamp):
    if isinstance(timestamp, (int, float)):
        return datetime.datetime.fromtimestamp(timestamp).date()
    raise ValueError(f'{timestamp} is incorrect time format, it should be timestamp (float num)')


class Task:
    __task_amount = 0

    def __new__(cls, *args, **kwargs):
        cls.__task_amount += 1
        return super().__new__(cls)

    def __init__(self, title: str, value='', task_priority=constansts.TASK_PRIORITIES['PRIORITY_3'],
                 scheduled_time: datetime = constansts.DEFAULT_SCHEDULED_TIME):
        self.__task_title = self._task_value = self.__task_priority = self.__task_scheduled_time = None
        self.__task_id = self.__task_amount
        self.__task_creation_time = datetime.datetime.timestamp(datetime.datetime.now())  #.strftime('%Y-%m-%d %H:%M:%S')
        self.set_title(title)
        self.set_value(value)
        self.set_priority(task_priority)
        self.schedule_time(scheduled_time)

    def schedule_time(self, time: float):
        if isinstance(time, (int, float)):
            self.__task_scheduled_time = time
        else:
            raise ValueError(f'{time} is incorrect time format, it should be timestamp (float num)')

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
