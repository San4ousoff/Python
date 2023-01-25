from datetime import *

time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

def write_data(data): # запись в лог-файл
    data = ''.join(map(str, data))
    with open('Seminar7/Homework/Phone/log.xml', 'a', encoding='utf=8') as file:
        file.write(f'{time}. {data}\n')

def read_log(): # чтение из лог-файла
    with open('Seminar7/Homework/Phone/log.xml', encoding='utf=8') as log_file:
        print(*log_file.readlines())