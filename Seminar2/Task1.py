# Напишите программу, которая принимает на вход число N и выдает последовательность из N случайных элементов

import random

number = int(input('Введите число: '))
for i in range(number):
    print(random.randrange(-100, 100), end=' ')
