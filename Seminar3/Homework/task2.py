# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import defs as df

num = int(input('Введите число: '))
lst = df.creat_list(num)
print(f'Исходный список: {lst}')
# Решение через вложенные циклы с i и j и range с отрицательным шагом - суммирование индексов пар (сумма 
# равна len-1)

# if len(lst)%2!=0:
#     for i in range(int(len(lst)/2+1)):
#         for j in range(0, int(-len(lst)/2-1), -1):
#             if i+j == 0:
#                 print(lst[i]*lst[j-1], end=' ')
# else:
#     for i in range(int(len(lst)/2)):
#         for j in range(0, int(-len(lst)/2), -1):
#             if i+j == 0:
#                 print(lst[i]*lst[j-1], end=' ')

# Решение (после оптимизации) через применение одного цикла с i - вычисление индекса парного элемента 
# с конца (len - 1 - i). Думаю, что можно еще оптимизировать код, но не хватает тямы...

print('Произведение пар чисел списка: ' , end='')
if len(lst)%2==0:
    for i in range(int(len(lst)/2)):
        print(lst[i] * lst[int(len(lst)-1-i)], end=' ')
else:
    for i in range(int(len(lst)/2)+1):
        print(lst[i] * lst[int(len(lst)-1-i)], end=' ')

