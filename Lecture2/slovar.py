# Словарь - неупорядоченная коллекция произвольных объектов с доступом к ключу
dictionary = {}
dictionary = \
    {
        'up': 'W',
        'left': 'A',
        'down': 'S',
        'right': 'D'
    }

print(dictionary)
print(dictionary['left'])

for k in dictionary.keys(): # список ключей
    print(k)

for k in dictionary.values(): # список значений
    print(k)