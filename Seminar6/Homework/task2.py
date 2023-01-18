# Задание 2 из Семинара 2 (применение map())

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math
import defs

num = int(input('Введите число: '))

for i in range(1, num+1):
    print(math.factorial(i), end=' ') # реализация через втроенный метод factorial

print()
for i in range(1, num+1):
    print(defs.factorial(i), end=' ') # реализация через метод factorial из файла defs.py
print()

# Применение map()
print('\nВариант с применением map()')
print(*map(defs.factorial, range(1,num+1)))