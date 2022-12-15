# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 
# 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import os
dot_a = ['X точки A: ','Y точки A: ']
dot_b = ['X точки B: ','Y точки B: ']
arr_a = []
for i in range(2):
    arr_a.append(int(input(f'Введите координату {dot_a[i]}')))
arr_b = []
for i in range(2):
    arr_b.append(int(input(f'Введите координату {dot_b[i]}')))
os.system('cls')
print(f'Координаты точки A: {arr_a}')
print(f'Координаты точки B: {arr_b}')
# import math
# segment_length = round(math.sqrt((arr_b[0]-arr_a[0])**2 + (arr_b[1]-arr_a[1])**2),2)
segment_length = round((((arr_b[0]-arr_a[0])**2 + (arr_b[1]-arr_a[1])**2)**0.5),2)
print(f'Длина отрезка между точками A и B = {segment_length}')