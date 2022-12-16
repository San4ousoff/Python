# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять 
# количество вхождений одной строки в другой.

str_1 = input()
str_2 = input()

in_num = str_1.count(str_2)

print(in_num)

# str_1 = 'sdfsdfsdfxcgvhdfghsdfgsdhdfghdfghdsfgdfbs' 
# str_2 = 'sdf'
# counter = 0
# for i in range(len(str_1) - len(str_2)):
#     flag = False
#     if str_2[0] == str_1[i]:
#         flag = True
#         for j in range(1,len(str_2)):
#             if str_2[j] != str_1[i + j]:
#                 flag = False
#         if flag:
#             counter += 1
# print(f'Вторая строка встречается в первой {counter} раз')

# str_1 = 'sdfsdfsdfxcgvhdfghsdfgsdhdfghdfghdsfgdfbs' 
# str_2 = 'sdf'
# counter = 0
# for i in range(len(str_1) - len(str_2)):
#     if str_2 == str_1[i: i + len(str_2)]:
#         counter += 1
# print(f'Вторая строка встречается в первой {counter} раз')

