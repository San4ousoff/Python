import logger as log

def view_entry(): # просмотр записей справочника
    temp_lst = []
    with open(r"Seminar7/Homework/Phone/phone_directory.txt", 'r', encoding="utf-8") as file:
        for line_numb, line in enumerate(file, start=1):
            temp_lst.append(str(line_numb) + '. ' + line[:(-1)])
    return line_numb, temp_lst

def add_entry(add_str=str): # добавление записи в справочник
    with open(r"Seminar7/Homework/Phone/phone_directory.txt", 'a', encoding="utf-8") as file:
        file.write(add_str)
    return

def find_entry(find_str=str): # поиск записи в справочнике
    result_find = []
    with open(r"Seminar7/Homework/Phone/phone_directory.txt", 'r', encoding="utf-8") as file:
        for line_numb, line in enumerate(file, start=1):
            if find_str in line:
                result_find.append(str(line_numb) + '. ' + line[:(-1)])
    return result_find

def del_entry(del_line=int): # удаление записи из справочника
    with open(r"Seminar7/Homework/Phone/phone_directory.txt", 'r', encoding="utf-8") as file:
        lines = file.readlines()
    print(f'Удалена строка: {lines[del_line - 1]}')
    log.write_data(f'Пользователь удалил запись: {lines[del_line - 1]}')
    del lines[del_line - 1]
    with open(r"Seminar7/Homework/Phone/phone_directory.txt", 'w', encoding="utf-8") as file:
        file.writelines(lines)
    
