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

# Проверка числа на "простоту" ;)
def prime_num(value):
    for i in range(2,value):
        if value%i == 0:
            break
        else:
            return(value)

# Создание списка [0, value1] из случайных чисел от 0 до value2
def creat_list_1(value1,value2):
    import random
    lst = []
    for i in range(0, value1):
        lst.append(random.randrange(0, value2))
    return(lst)

# Рандомное создание полинома с коэффициентами от 0 до 100 при входящей степени (k)
def creat_polynom(k):
    from random import randint
    import itertools

    lst = list([randint(0, 100) for i in range(k+1)])
    print(f'Список коэффициентов: {lst}')
    mask = ['*x^']*(k-1) + ['*x']
    polynomynom = [[a, b, c] for a, b, c in itertools.zip_longest(lst, mask, range(k, 1, -1), fillvalue='')]
    for x in polynomynom:
        x.append(' + ')
    polynomynom = list(itertools.chain(*polynomynom))
    polynomynom[-1] = ' = 0'
    return "".join(map(str, polynomynom)).replace(' 1*x',' x')

# Забрать данные из определенного файла
def take_data(file):
    with open(str(file), 'r') as data:
        result = data.read()
    return result

# Разборка полинома на коэффициенты и степени
def dismantling_polynom(polynom):
    import re

    polynom = polynom.replace('= 0', '') # убрали хвост
    polynom = re.sub("[*|^| ]", " ", polynom).split('+') 
    polynom = [char.split(' ') for char in polynom]
    polynom = [[x for x in list if x] for list in polynom]
    for i in polynom:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    polynom = [tuple(int(x) for x in j if x != 'x') for j in polynom]
    return polynom