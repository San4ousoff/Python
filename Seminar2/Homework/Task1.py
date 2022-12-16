# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

for i in range(3):
    number = input(f'Введите число ({i} попытки): ')
    if isfloat(number):
        print('Это число')
    else:
        print('Это не число')