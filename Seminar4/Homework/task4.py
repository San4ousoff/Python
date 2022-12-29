# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools

k = int(input('Задайте натуральную степень k: '))

lst = list([randint(0, 100) for i in range(k+1)])
print(f'Список коэффициентов: {lst}')
mask = ['*x^']*(k-1) + ['*x']
polynom = [[a, b, c] for a, b, c in itertools.zip_longest(lst, mask, range(k, 1, -1), fillvalue='')]
#print(polynom)
for x in polynom:
    x.append(' + ')
polynom = list(itertools.chain(*polynom))
#print(polynom)
polynom[-1] = ' = 0'
#print(polynom)
polynom_str = "".join(map(str, polynom)).replace(' 1*x',' x')
print(f'То, что улетело в файл: {polynom_str}')

# from defs import creat_polynom as cp
# k = int(input('Задайте натуральную степень k: '))
# polynom_str = cp(k)
# print(polynom_str)

with open('Seminar4/Homework/task4.txt', 'w') as data:
    data.write(polynom_str)