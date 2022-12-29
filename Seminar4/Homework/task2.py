# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

#from defs import prime_num as pn

num = int(input('Введите число: '))
lst=[]

for i in range(2,num+1):
    if num % i == 0:
        count = 1
        for j in range(2,(i//2+1)):
            if(i%j==0):
                count=0
                break
        if (count==1):
            lst.append(i)
print(f'Список простых множителей числа "{num}": {lst}')