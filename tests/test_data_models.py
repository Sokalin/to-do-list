from src.data_models import Task


def test_main():
    task = Task('none')
    assert type(task.get_data()[1]) == int
