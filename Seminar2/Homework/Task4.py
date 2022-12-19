# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной 
# строке одно число.

import defs

num = int(input('Введите число: '))
list = defs.creat_list(num)

print(list)
path = 'Seminar2/Homework/file.txt'
data = open(path)
a = int(data.readline())
b = int(data.readline())
print(f'Элемент списка с индексом {a} = {list[a]}')
print(f'Элемент списка с индексом {b} = {list[b]}')
print(f'Их произведение равно {list[a]*list[b]}')
data.close()
exit()