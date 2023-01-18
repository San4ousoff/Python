# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import os
from defs import take_data as td

def encoder(data):
    encode = ''
    pre_char = ''
    counter = 1
    if not data: return ''
    for char in data:
        if char != pre_char:
            if pre_char:
                encode += str(counter) + pre_char
            counter = 1
            pre_char = char
        else:
            counter += 1
    else:
        encode += str(counter) + pre_char
    return encode

def decoder(data):
    decode = ''
    counter = ''
    for char in data:
        if char.isdigit(): 
            counter += char
        else:
            decode += char * int(counter)
            counter = ''
    return decode

while True:
    os.system('cls')
    print("1. Проверка работы метода RLE-кодирования")
    print("2. Проверка работы метода RLE-декодирования")
    print("0. Выход")
    cmd = input("Выберите пункт: ")
    if cmd == "1":
        data = td('Seminar5/Homework/encoded.txt')
        print(f'Данные из файла encoded.txt для кодировки: {data}')
        encoded_val = encoder(data)
        with open('Seminar5/Homework/decoded.txt', 'w') as data:
            data.write(encoded_val)
        data = td('Seminar5/Homework/decoded.txt')
        print(f'Закодированные данные из файла decoded.txt: {data}')
        input('---Нажмите Enter---')
    elif cmd == "2":
        data = td('Seminar5/Homework/decoded.txt')
        print(f'Данные из файла decoded.txt для декодировки: {data}')
        decoded_val = decoder(data)
        with open('Seminar5/Homework/encoded.txt', 'w') as data:
            data.write(decoded_val)
        data = td('Seminar5/Homework/encoded.txt')
        print(f'Раскодированные данные из файла encoded.txt: {data}')
        input('---Нажмите Enter---')
    elif cmd == "0":
        break
    else:
        print("Вы ввели неправильное значение")
        input('---Нажмите Enter---')