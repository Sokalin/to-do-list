import data_models


if __name__ == '__main__':
    a1 = data_models.TaskPriority1('sleep')
    a1.show_data()
    a2 = data_models.TaskPriority1('drink coffe')
    a2.show_data()
    a3 = data_models.TaskPriority3()
    a3.show_data()

    for a in [a1, a2, a3]:

        a.show_data()

