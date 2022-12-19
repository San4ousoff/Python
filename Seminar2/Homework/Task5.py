# Реализуйте алгоритм перемешивания списка.

import defs

num = int(input('Введите число: '))

list = defs.creat_list(num)
mixed_list = defs.mix_list(list)
print(f"Исходный список: {list}")
print(f"Перемешанный список: {mixed_list}")