# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 
#     *Пример:* 
#     2+2 => 4; 
#     1+2*3 => 7; 
#     1-2*3 => -5;
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
#         *Пример:* 
#         1+2*3 => 7; 
#         (1+2)*3 => 9;
def calc(my_list):

    if '*' in my_list or '/' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '*':
                result = my_list.pop(i+1) * my_list.pop(i-1)
                my_list[i-1] = result
            elif my_list[i] == '/':
                result = my_list.pop(i+1) / my_list.pop(i-1)
                my_list[i-1] = result

    if '+' in my_list or '-' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '-':
                result = my_list.pop(i+1) - my_list.pop(i-1)
                my_list[i-1] = result
            elif my_list[i] == '+':
                result = my_list.pop(i+1) + my_list.pop(i-1)
                my_list[i-1] = result
    
    return my_list
   
s = '3*(10+12)'
num = ''
old_list = []
for elem in s:
    if elem.isdigit():
        num += elem
    elif elem in '()':
        old_list.append(elem)
    else:
        old_list.append(int(num))
        old_list.append(elem)
        num = ''
if s[-1] == ')':
    old_list.insert(-1, int(num))
else:    
    old_list.append(int(num))

if '(' in old_list:
    first_i = old_list.index('(')
    second_i = old_list.index(')')
    old_list = old_list[:first_i] + calc(old_list[first_i+1:second_i]) + old_list[second_i+1:]

old_list = calc(old_list)
print(old_list)


# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:* 
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
from random import *

res = [randint(1, 10) for i in range(8)]
print('Задали список: ', res, '\n')

res_1 = list(filter(lambda x: res.count(x) == 1, res))
res_2 = [i for i in res if res.count(i) == 1]
res_3 = list(set(res))

print('Список уникальных элементов: ', res_1)
print('Список уникальных элементов: ', res_2)
print('Список уникальных элементов: ', res_3, '\n')
