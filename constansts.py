import datetime

MAX_STRING_LEN = 100
DEFAULT_SCHEDULED_TIME = datetime.datetime.timestamp(datetime.datetime.now() + datetime.timedelta(days=1))
TASK_PRIORITIES = {'PRIORITY_1': 1, 'PRIORITY_2': 2, 'PRIORITY_3': 3}
SQLITE3_DATA_TYPES = ('INTEGER', 'FLOAT', 'TEXT', 'BOOL')  # уточнить какие могут быть типы данных
