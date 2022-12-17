# Использование функций из других файлов
# import Seminar2/Homework/Task1
# print(task1.isfloat(2.22))

# def new_string(symbol, count):
# def new_string(symbol, count = 3): # можноприсвоить жестко значение
#     return symbol * count

# print (new_string('!', 5)) # !!!!!
# print (new_string('!'))    # !!!
# print (new_string(4))      # 12

def concatenetio(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenetio('a', 's', 'd', 'w')) # asdw
print(concatenetio('a', '1')) # a1