from export_data import *
from import_data import *
import actions_files as af
import check as ch
import logger as lg

def user_choose():
    ch.clear()
    af.receive_entry()
    print('''<<< Справочник школы - главное меню>>> 
    
                <1> Добавить ученика и класс
                <2> Удалить ученика   
                <3> Редактировать данные ученика
                <4> Просмотр справочника
                -----
                <5> Перевести ученика в другой класс
                <6> Удалить класс
                ---
                <7> Просмотр log-файла
                <8> Экспорт справочника
                ---
                <9> Выход''')
    choose = input('\nВведите номер пункта меню: ')
    lst_num = list(map(str, range(1,10)))
    if ch.check_1(choose, lst_num) is True:
        if choose == '9': # выход
            print('\nДо свидания!') 
            ch.press_key()
            exit()
        if choose == '1': # добавить
            ch.clear()
            create_student()
            print()
            ch.press_key()
            user_choose()
        elif choose == '2': # удалить ученика
            ch.clear()
            delete_student()
            print()
            ch.press_key()
            user_choose()
        elif choose == '3': # редактировать данные по ученику
            ch.clear()
            edit_student()
            print()
            ch.press_key()
            user_choose()
        elif choose == '4': # просмотр
            ch.clear()
            to_console()
            print()
            ch.press_key()
            user_choose()
        elif choose == '5': # перевести ученика в другой класс
            ch.clear()
            edit_class()
            print()
            ch.press_key() 
            user_choose()
        elif choose == '6': # удалить класс
            ch.clear()
            delete_class()
            print()
            ch.press_key()
            user_choose()
        elif choose == '7': # просмотр log
            ch.clear()
            print('<<< Просмотр лог-файла>>>')
            lg.write_data('Пользователем осуществлен просмотр лог-файла')
            print('\nЛог-файл:')
            lg.read_log()
            print()
            ch.press_key()
            user_choose()
        elif choose == '8':
            ch.clear()
            to_file()
            print()
            ch.press_key()
            user_choose()
    else:
        print(f'\nТакого пункта меню {choose} не существует. Повторите ввод!\n')
        user_choose()
