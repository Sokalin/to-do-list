from src.task_manager import TaskManager
import datetime

if __name__ == '__main__':
    task_manager = TaskManager()
    task_manager.create_task('do nothing', 'just do it', 1)
    task_manager.create_task('BEST TASK', 'do nothing', 3,
                             datetime.datetime.timestamp(datetime.datetime(2024, 7, 13, 23, 59, 59)))
    task_manager.create_task('sleep and drink coffee',
                             scheduled_time=datetime.datetime.timestamp(datetime.datetime(2024, 7, 14, 0, 0, 0)))
    print(f'today\'s task are {[x[2] for x in task_manager.get_today_tasks()]}')
    print(f'all tasks are {[x[2] for x in task_manager.get_all_tasks()]}')
    task_manager.del_task('title == "BEST TASK"')
    task_manager.update_task({'title': 'NEW BEST TASK'}, 'title == "do nothing"')
    print(f'all tasks are {[x[2] for x in task_manager.get_all_tasks()]}')
