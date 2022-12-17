# colors = ['red', 'green', 'blue1']
# # data = open('file.txt', 'a') # данные добавляются
# data = open('file.txt', 'w') # данные перезаписваются
# data.writelines(colors)
# data.write('\nLine 2\n') # добавление второй строки с переносом
# data.write('Line 3\n') # добавление третьей строки с переносом
# data.close()

# Второй вариант создания файла и записи в него данных
# with open('file.txt', 'w') as data:
#     data.write('Line 1\n')
#     data.write('Line 2\n')

# Чтение из файла
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line, end='')
data.close()

exit()
