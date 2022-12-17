# Списки

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1[0] = 123
# list2[2] = 333

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

list1 = [1, 2, 3, 4, 5]

print(len(list1))
print(list1)
print(list1.pop()) # удаление последнего элемента списка
print(list1)
print(list1.pop(0)) # удаление конкретного элемента списка
print(list1)
print(list1.insert(2, 11)) # вставка конкретного элемента в конкретное место в списке
print(list1)
print(list1.append(22)) # вставка конкретного элемента в конец списка
print(list1)