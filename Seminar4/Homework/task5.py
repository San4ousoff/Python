# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from defs import take_data as td
from itertools import zip_longest, chain

file_1 = 'Seminar4/Homework/task5_1.txt'
file_2 = 'Seminar4/Homework/task5_2.txt'
 
def convert_pol(pol):  # Метод для удаления "=0" и разложения строки (вход: формула полинома)
    pol.replace('= 0', '')
    pol = pol.split(' + ')
    pol = [i[0] for i in pol]
    for i in range(len(pol)):
        if pol[i] == 'x':
            pol[i] = '1'
            pol = pol[::-1]
        return pol

def get_polynomial(k, ratios):  # Метод для сборки полинома (вход: степень, массив коэффициентов)
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in zip_longest(ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')

pol1, pol2 = td(file_1), td(file_2) # забрали из файлов
print('Исходные полиномы:', pol1, pol2, sep='\n')
pol1_coef, pol2_coef = list(map(int, convert_pol(pol1))), list(map(int, convert_pol(pol2)))
sum_coef = list(map(sum, zip_longest(pol1_coef, pol2_coef, fillvalue=0)))
sum_pol = get_polynomial(len(sum_coef)-1, sum_coef)
print('Сумма исходных полиномов:', sum_pol, sep='\n')

with open('Seminar4/Homework/task5_1+2.txt', 'w') as data:
    data.write(sum_pol) # положили в файл