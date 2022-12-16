# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#    *Пример:*
#    - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# my_dict = {1: 4, 2: 7, 'sdffs': 10, 4: 13, 5: 16, 6: 19}

# 1) все ключи, уникальные
# 2) ключами могут быть только неизменяемые типы данных
# 3) значенииями могут быть любые типы данных
# 4) неупорядоченные

# # print(my_dict['sdffs'])
# print(my_dict[2])
# # 5) dict() - словарь
# # list() - список

# my_list = [[1, 4], [2, 7], ['sdffs', 10]]
# my_list = ([1, 4], [2, 7], ['sdffs', 10])
# my_list = [(1, 4),(2, 7), ('sdffs', 10)]
# my_list = ((1, 4),(2, 7), ('sdffs', 10))
# new_dict = dict(my_list)

number = int(input('Введите число: '))
diction = []
for i in range(1, number+1):
    diction.append([i, 3*i+1])
print(dict(diction))

# n = int(input("Введите число: "))
# diction = {}
# for i in range(1, n+1):
#     dict.update({i:3*i+1}) 
#     # dict[i] = 3*i+1
# print(dict)
