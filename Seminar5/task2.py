# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую 
# последовательность. Порядок элементов менять нельзя.
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

my_list = [1, 5, 2, 3, 4, 6, 1, 7]
new_list = list()
new_list.append(my_list[0])
print(len(new_list))

for index, elem in enumerate(my_list):
    if elem > new_list[-1]:
        new_list.append(elem)

print(new_list)
