import check as ch
import actions_files as af
import export_data as ed
import user_interface as ui
import logger as lg

myDict = {}

def from_file():
    pass

# Добавление ученика и класса. Если класса нет, добавляем и его с новым учеником.
def create_student():
    my_dict = af.receive_entry()
    print('<<< Добавление ученика и класса >>>\n')
    name_class = input('Введите класс: ')
    name_stud = input('Введите ФИО ученика: ')
    comm_stud = input('Введите данные: ')
    if name_class in my_dict: # - можно ли сделать через setdefault()?
        my_dict[name_class][name_stud] = comm_stud
    else:
        temp_dict={}
        temp_dict[name_stud] = comm_stud
        my_dict[name_class] = temp_dict
    af.add_entry(my_dict)
    print(f'\nВ {name_class} добавлена запись ученика: {name_stud} : {comm_stud}')
    lg.write_data(f'В {name_class} добавлена запись ученика: {name_stud} : {comm_stud}')

def edit_student():
    print('<<< Редактирование данных ученика >>>\n')
    ed.to_console()
    edit_dict = af.receive_entry()
    name_class = input('\nДля редактирования данных ученика введите класс: ')
    name_stud = input('и фамилию ученика: ')
    value = input('Введите новые данные по ученику: ')
    edit_dict[name_class][name_stud] = value
    print(f'В справочнике внесены новые данные по ученику {name_stud} из {name_class}')
    lg.write_data(f'В справочнике внесены новые данные по ученику {name_stud} из {name_class}')
    af.add_entry(edit_dict)

def delete_student():
    ch.clear
    print('<<< Удаление ученика >>>\n')
    ed.to_console()
    del_dict = af.receive_entry()
    name_class = input('\nДля удаления записи ученика введите класс: ')
    name_stud = input('и фамилию ученика: ')
    del (del_dict[name_class][name_stud])
    print(f'Из справочника удалены данные ученика {name_stud} из {name_class}')
    lg.write_data(f'Из справочника удалены данные ученика {name_stud} из {name_class}')
    af.add_entry(del_dict)

def delete_class():
    print('<<< Удаление класса >>>\n')
    ed.to_console()
    del_dict = af.receive_entry()
    name_class = input('\nВведите класс для удаления: ')
    del (del_dict[name_class])
    print(f'Из справочника удален класс {name_class}')
    lg.write_data(f'Из справочника удален класс {name_class}')
    af.add_entry(del_dict)

def edit_class():
    print('<<< Перевод ученика в другой класс >>>\n')
    ed.to_console()
    edit_dict = af.receive_entry()
    name_class = input('\nДля перевода ученика введите его класс: ')
    name_stud = input('и фамилию ученика: ')
    key = input('Введите новый класс ученика: ')
    if key not in edit_dict.keys():
        print('Вам необходимо добавить класс!')
        ui.create_student()
        edit_class()
    edit_dict[key][name_stud] = edit_dict[name_class][name_stud]
    print(f'Ученик {name_stud} переведен из {name_class} в {key}')
    lg.write_data(f'Ученик {name_stud} переведен из {name_class} в {key}')
    af.add_entry(edit_dict)
