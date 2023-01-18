# Задание 1 из Семинара 5 (применение list comprehension, lambda, filter())

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str = 'ывдлк пдпджк Абвплл вАБВппп выууыабВ впвап'
print(f'Исходная строка: {str}')
data = str.lower().split()
out_data = []
for i in range(len(data)):
    if 'абв' not in data[i]:
        out_data.append(data[i])
str = ' '.join(out_data)
print(f'Строка без слов с "абв": {str}')

# Применение lambda, filter()
print('\nВариант 1. Применение lambda, filter()')
str = 'лдофы  фдылабв  аБв дловфы абвыдфлоф'
print(f'Исходная строка: {str}')
str = ' '.join(list(filter(lambda x: not 'абв' in x.lower(), str.split())))
print(f'Строка без слов с "абв": {str}')

# Применение list comprehension
print('\nВариант 2. Применение list comprehension')
str = 'АБвппп прнисаб фыфыабвпарпр вбапррпр абв вавапвп'
print(f'Исходная строка: {str}')
data = str.lower().split()
out_data = ''
str = ' '.join([out_data + el for el in data if 'абв' not in el])
print(f'Строка без слов с "абв": {str}')