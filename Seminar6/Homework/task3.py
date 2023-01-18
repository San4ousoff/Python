# Задание 1 из Семинара 3 (применение enumerate())

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import defs as df

num = int(input('Введите число: '))
lst = df.creat_list(num)

print(f'Исходный список: {lst}')
sum = 0
for i in range(len(lst)):
    if i%2!=0:
        sum += lst[i]

print(f'Сумма элементов на нечетных позициях с range() = {sum}')

# Замена цикла с range() на цикл с enumerate()
sum = 0
for count, elem in enumerate(lst):
    if count%2!=0:
        sum += elem
print(f'Сумма элементов на нечетных позициях c enumerate() = {sum}')