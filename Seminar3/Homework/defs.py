# Защита от дурака (Проверка введенного значения на соответствие условию float)
# def isfloat(value):
#     try:
#         float(value)
#         return True
#     except ValueError:
#         return False

# Сумма цифр числа
def sum_of_digits(value):
    summa = 0
    while value != 0:
        summa = summa + (value % 10)
        value = value // 10
    return(summa)       

# Факториал заданного числа
def factorial(value):
    fact = 1
    for value in range(2, value + 1):
        fact *= value
    return fact

# Создание списка [-value, value] из случайных чисел от -10 до 10
def creat_list(value):
    import random
    list = []
    for i in range(-value, value+1):
        list.append(random.randrange(-10, 10))
    return(list)

# Алгоритм перемешивания списка
import random
def mix_list(value):
    list_mix = value[:]
    for i in range(len(list_mix)):
        index_rand = random.randint(0, len(list_mix) - 1)
        temp = list_mix[i]
        list_mix[i] = list_mix[index_rand]
        list_mix[index_rand] = temp
    return list_mix

# Вычисление двоичного числа из десятичного
def dec_2_bin(value):
    bn = ''
    while value > 0:
        bn += str(value % 2)
        value = value // 2
    return bn