# Вывод в консоль
# Вывод в файл

import import_data as id
import export_data as ed
import actions_files as af
import logger as lg
import check as ch

def to_console():
    print('<<< Просмотр >>>\n')
    print_dict = af.receive_entry()
    for key,value in print_dict.items():    
        print(key, ':')
        for k, v in value.items():
            print(k, ':', v)
    lg.write_data(f'Осуществлен просмотр справочника')

def to_file():
    print('<<< Зкспорт в файл >>>\n')
    exp_dict = af.receive_entry()
    with open('Seminar8/Homework/New/export.xml', 'w', encoding='utf=8') as file:
        for key, value in exp_dict.items():
            key_str = key + ':\n'
            file.write(key_str)
            for k, v in value.items():
                k_str = k + ' - ' + v + '\n'
                file.write(k_str)
    print('Экспорт завершен\n')
    lg.write_data(f'Осуществлен экспорт справочника')
    