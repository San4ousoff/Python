# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех 
# значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            result = not (x or y or z) == (not x and not y and not z)
            if result == True:
                print(x, y, z, 'Утверждение истинно')
            else:
                print(x, y, z, '"Утверждение ложно')