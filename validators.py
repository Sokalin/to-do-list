import constansts
import datetime


def validate_text(func):
    def wrapper(self, text, *args, **kwargs):
        if len(str(text)) <= constansts.MAX_STRING_LEN:
            func(self, text, *args, **kwargs)
        else:
            raise ValueError(f'Value {text} is inappropriate for MAX_STRING_LEN = {constansts.MAX_STRING_LEN}')

    return wrapper


def validate_time(func):
    def wrapper(self, time, *args, **kwargs):
        if isinstance(time, datetime.datetime) and time >= datetime.datetime.now():
            func(self, time)
        else:
            raise ValueError(f'{time} is incorrect time format')

    return wrapper
