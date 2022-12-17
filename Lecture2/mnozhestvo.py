# Множество

colors = {'red', 'green', 'blue'}
print(type(colors))

# colors.add - добавить элемент
# colors.remove - удалить элемент
# colors.discard - удалить элемент, даже если его нет (без ошибки)
# colors.clear - очистить список

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # копирование 
u = a.union(b) # объединение {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # пересечение {8, 2, 5}
dl = a.difference(b) #  {1, 3} исключение
dr = b.difference(a) #  {13, 21} исключение