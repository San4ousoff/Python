# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))

negofib=[1, 0, 1]

# Два фора
# for i in range(1,n):
#     negofib.append(negofib[i]+negofib[i+1])
# for i in range(0,-n+1,-1):
#     a = negofib[1]-negofib[0]
#     negofib.insert(0, a)

# Один фор
for _ in range(1, n):
    negofib.append(negofib[-2] + negofib[-1])
    negofib.insert(0, negofib[1] - negofib[0])

print(f'Числа Фибоначчи для {n}: {negofib}')