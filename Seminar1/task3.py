# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#     *Примеры:* 
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

num = int(input('Введите положительное число: '))
for number in range(-num,num+1):
    print(number, end=', ')

# Примеры применения print
# word = 'python'
# print(*word)
# print(*word, sep='-', end=' ')
# print(*word, sep='-', end='\n')
# print(*word, sep='\n')

# через list
# num = int(input('Введите положительное число: '))
# my_list = range(-num, num + 1)
# print(*my_list, sep=', ')
# print(list(my_list))