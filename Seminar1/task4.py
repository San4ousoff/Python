# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

num = float(input("введите число: "))
if num%1==0:
    print ("нет")
else:
    print(int(num * 10 % 10))

# num = float(input("введите число: ")) 
# num_check = num%1
# if num_check ==0:
#     print ("нет")
# else:
#     num_1 = num * 10 
#     num_2 = num_1% 10
#     num_3 = int(num_2)
#     print(num_3)
# num_1 = '122.45'
# num_2 = '45'

# print('.' in num_1)
# print('.' not in num_2)

# print(num_1.isdigit())
# print(not num_2.isdigit())
