# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

def find_index_coin(new_list, text, num=2):
    count = 0
    for i in range(len(new_list)):
        if text == new_list[i]:
            count += 1
        if count == num:
            return i
    return -1

my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(find_index_coin(my_list, 'qwe'))

# Без функции
# new_list = ["qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"]
# text = 'qwe2'
# num = 2 # позиция какого вхождениия нам нужно найти
# count = 0
# for i in range(len(new_list)):
#     if text == new_list[i]:
#         count += 1
#         if count == num:
#             print('Позиция второго вхождения - ',i)
#             break
# else:
#     print(-1)

