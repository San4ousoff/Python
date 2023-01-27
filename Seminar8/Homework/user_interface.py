from export_data import *
from import_data import *
import check as ch


def user_choose():
    ch.clear()
    print('''<<< Справочник школы - главное меню>>> 
    
                <1> Добавить ученика   
                <2> Редактировать данные ученика   
                <3> Удалить ученика
                <4> Просмотр данных ученика
                -----
                <5> Перевести ученика в другой класс
                <6> Добавить класс
                ---
                <7> Импорт
                <8> Экспорт
                <9> Выход''')
    choose = input("Введите номер пункта меню: ")
    lst_num = list(map(str, range(1,10)))
    if ch.check_1(choose, lst_num) is True:
        if choose == '9': # выход
            print('\nДо свидания!') 
            ch.press_key()
            exit()
        if choose == '1':
            create_student()
            user_choose()
        elif choose == '2':
            edit_student()
            user_choose()
        elif choose == '3':
            delete_student()
            user_choose()
        elif choose == '4':
            to_console()
            user_choose()
        elif choose == '5':
            change_class()
            user_choose()
        elif choose == '6':
            create_cl()
            user_choose()
        elif choose == '7':
            from_file()
            user_choose()
        elif choose == '8':
            to_file()
            user_choose()
    else:
        print(f'\nТакого пункта меню {choose} не существует. Повторите ввод!\n')
        user_choose()
