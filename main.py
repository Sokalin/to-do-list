import data_models
from database import DataBaseManager

if __name__ == '__main__':
    with DataBaseManager('tasks.db') as DataBase:
        DataBase.delete_all_tables()
        DataBase.get_info()
        DataBase.create_table('jkjkj', {'id': 'INTEGER', 'name': 'TEXT', 'surname': 'TEXT'})
        DataBase.get_info()
        DataBase.add_record('jkjkj', [1, 'jhon', 'doe'])

    a1 = data_models.Task('task title', 'subtitle', 1)
