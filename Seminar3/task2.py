# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое 
# число.

# my_list =["123", "234", 123, "567"]

# if 123 in my_list:
#     print('Да')

array = ["12", "222", "90", "6", "98"]
print(array)

num = input("Введите число: ")

if num in array:
    print("Да")
else:
    print("Нет")