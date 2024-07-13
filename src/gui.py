import tkinter
from task_manager import TaskManager
import datetime

task_manager = TaskManager()
task_manager.create_task('do nothing', 'just do it', 1)
task_manager.create_task('BEST TASK', 'do nothing', 3,
                         datetime.datetime.timestamp(datetime.datetime(2024, 7, 13, 23, 59, 59)))
task_manager.create_task('sleep and drink coffee',
                         scheduled_time=datetime.datetime.timestamp(datetime.datetime(2024, 7, 14, 0, 0, 0)))

root = tkinter.Tk()


def show_today_tasks():
    main_text['text'] = '\n'.join([f'{x[2]} ({x[3]})' for x in task_manager.get_today_tasks()])


def show_all_tasks():
    main_text['text'] = '\n'.join([f'{x[2]} ({x[3]})' for x in task_manager.get_all_tasks()])


root.title("Task manager")
root.geometry("800x400+600+300")
root.resizable(width=False, height=False)
main_text = tkinter.Label()
all_tasks = tkinter.Button(text='Show all tasks', command=show_all_tasks)
today_tasks = tkinter.Button(text='Show today\'s tasks', command=show_today_tasks)


all_tasks.grid(row=1, column=1)
today_tasks.grid(row=1, column=2)
main_text.grid(row=2, columnspan=2)

root.mainloop()
