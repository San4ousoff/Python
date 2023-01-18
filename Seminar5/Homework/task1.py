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

exit()

# Для ДЗ семинара 6 - lambda, filter
print('Вариант 1.')
st = 'лдофы  фдылабв  аБв дловфы абвыдфлоф'
print(f'Исходная строка: {st}')
st = ' '.join(list(filter(lambda x: not 'абв' in x.lower(), st.split())))
print(f'Строка без слов с "абв": {st}')

# Для ДЗ семинара 6 - list comprehension
print('\nВариант 2.')
str = 'АБвппп прнисаб фыфыабвпарпр вбапррпр абв вавапвп'
print(f'Исходная строка: {str}')
data = str.lower().split()
out_data = ''
str = ' '.join([out_data + el for el in data if 'абв' not in el])
print(f'Строка без слов с "абв": {str}')