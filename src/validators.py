from src import constansts


def validate_time_data(year, month, day, hour, minute, second):
    if type(year) == type(month) == type(day) == type(hour) == type(minute) == type(second) == int \
           and year >= 1971 and 1 <= month <= 12 and 1 <= day <= 31 \
           and 0 <= hour <= 23 and 0 <= minute <= 60 and 0 <= second <= 60:
        pass
    else:
        raise ValueError(f'Uncorrected date input {year, month, day, hour, minute, second}')


def validate_text(func):
    def wrapper(self, text, *args, **kwargs):
        if len(str(text)) <= constansts.MAX_STRING_LEN:
            func(self, text, *args, **kwargs)
        else:
            raise ValueError(f'Value {text} is inappropriate for MAX_STRING_LEN = {constansts.MAX_STRING_LEN}')

    return wrapper

