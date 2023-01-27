import msvcrt as m
import os

clear = lambda: os.system('cls')

def check_1(num, lst): # проверка num - цифра, попадает в список lst
    return len(num) == 1 and num.isdigit() and num in lst

def press_key(): # ожидание нажатия клавиши с надписью
    print('Нажмите любую клавишу...')
    m.getch()
    clear()

# def check_2(user_vol, str_1, str_2): # проверка введенных пользователем данных на соответствие str_1 или str_2
#     return len(user_vol) == 1 and user_vol.isalpha() and user_vol.lower() == str_1.lower or user_vol.lower() == str_2.lower