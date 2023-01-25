import check as ch
import actions_entry as ae
import actions_file as af
import logger as log

def menu_view():
    ch.clear()
    print('<<< Просмотр >>>')
    log.write_data('Пользователем осуществлен просмотр')
    print('\nТелефонный справочник:')
    print('  ', 'Имя ', 'Фамилия ', 'Номер телефона ', 'Примечание ')
    last_num, lst_tel = ae.view_entry()
    for view in lst_tel:
        print(view)
    ch.press_key()

def menu_add():
    ch.clear()
    print('<<< Добавление >>>')
    add_str = (input(f'\nВведите имя: ') + ' ' +
               input(f'Введите фамилию: ') + ' ' +
               input(f'Введите номер: ') + ' ' +
               input(f'Введите примечание: ') + '\n')
    ae.add_entry(add_str)
    log.write_data(f'Пользователь добавил запись: {add_str[:-1]}')
    print('\nЗапись добавлена.')
    ch.press_key()

def menu_search():
    ch.clear()
    print('<<< Поиск >>>')
    find_str = input(f'\nВведите запрос: ')
    log.write_data(f'Пользователь осуществлял поиск: {find_str}')
    if len(ae.find_entry(find_str)) == 0:
        print('\nИскомый запрос отсутствует.')
    else:
        print('Результат поиска: ')
        for find_line in ae.find_entry(find_str):
            print(find_line)
    ch.press_key()

def menu_del():
    ch.clear()
    print('<<< Удаление >>>')
    last_num, lst_tel = ae.view_entry()
    print('\nТелефонный справочник:')
    print('  ', 'Имя ', 'Фамилия ', 'Номер телефона ', 'Примечание ')
    for view in lst_tel:
        print(view)

    print('''\nУверены, что хотите удалить запись? (Да/Нет) \n''')
    temp_imp = input('Введите ответ [Д/Н]: ')
    if temp_imp.lower() == 'д':
        numb_del = input("\nВведите порядковый номер строки для удаления: ")
        if numb_del.isdigit() and int(numb_del) <= last_num: 
            ae.del_entry(int(numb_del))
            ch.press_key()
        else:
            print(f'\nСтроки с номером {numb_del} нет в справочнике. Повторите ввод!\n')
            ch.press_key()
            menu_del()
    elif temp_imp.lower() == 'н': main_menu()

def menu_export_1():
    ch.clear()
    print('<<< Экспорт (записи через Enter) >>>')
    af.export_directory_1()
    print('\nЭкспорт осуществлен.')
    log.write_data('Пользователем осуществлен экспорт (записи через Enter)')
    ch.press_key()

def menu_export_2():
    ch.clear()
    print('<<< Экспорт (записи через ***) >>>')
    af.export_directory_2()
    print('\nЭкспорт осуществлен.')
    log.write_data('Пользователем осуществлен экспорт (записи через ***)')
    ch.press_key()

def menu_import():
    ch.clear()
    print('<<< Импорт >>>')
    print('''\nУбедитесь, что Ваш файл:
          - import.txt в корневой папке
          - разделители между элементами - пробел
          Всё верно? (Да/Нет) \n''')
    temp_imp = input('Введите ответ [Д/Н]: ')
    if temp_imp.lower() == 'д':
        af.import_file()
        print('\nИмпорт осуществлен.')
        log.write_data('Пользователем осуществлен импорт')
        ch.press_key()
    elif temp_imp.lower() == 'н': main_menu()
    else:
        print(f'Вы ввели некорректный ответ. Повторите ввод!')
        ch.press_key()
        menu_import()

def menu_log():
    ch.clear()
    print('<<< Просмотр лог-файла>>>')
    log.write_data('Пользователем осуществлен просмотр лог-файла')
    print('\nЛог-файл:')
    log.read_log()
    # last_num, lst_tel = ae.view_entry()
    # for view in lst_tel:
    #     print(view)
    ch.press_key()

def main_menu():
    ch.clear()
    print('''Главное меню:
    <1> Просмотр записей справочника
    <2> Добавление записи в справочник
    <3> Поиск записи в справочнике
    <4> Удаление записи из справочника
    -----
    <5> Экспорт справочника (записи через Enter)
    <6> Экспорт справочника (записи через ***)
    <7> Импорт справочника
    ----
    <8> Просмотр лог-файла
    <9> Выход''')
    
    num_menu = input(f'Введите номер пункта меню: ')
    lst_num = list(map(str, range(1,10)))
    if ch.check_1(num_menu, lst_num) is True:
        if num_menu == '9': # выход
            print('\nДо свидания!') 
            ch.press_key()
            exit()
# Действия с записями справочника 
        elif num_menu == '1':  # просмотр
            menu_view()
            main_menu()
        elif num_menu == '2':  # добавление
            menu_add()
            main_menu()
        elif num_menu == '3':  # поиск
            menu_search()
            main_menu()
        elif num_menu == '4':  # удаление
            menu_del()
            main_menu()
# Действия с файлами
        elif num_menu == '5': # экспорт Enter
            menu_export_1()
            main_menu()
        elif num_menu == '6': # экспорт ***
            menu_export_2()
            main_menu()
        elif num_menu == '7': # импорт
            menu_import()
            main_menu()
# Действия с лог-файлом
        elif num_menu == '8': # просмотр лога
            menu_log()
            main_menu()
    else:
        print(f'\nТакого пункта меню {num_menu} не существует. Повторите ввод!\n')
        main_menu()



