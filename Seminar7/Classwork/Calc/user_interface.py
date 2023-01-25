import logger

# x = 0
# y = 0

# def init(a, b): # блок инициализации данных
#     global x
#     global y
#     x = a
#     y = b

def get_data(): # метод получения данных
    a = input('Введите число: ') # вводим строчные значения, чтобы потом их конвертировать в нужный формат
    b = input('Введите число: ')
    operator = input('Введите действие: ')
    
    logger.log_all(f'Мы получаем число {a}, оператор = "{operator}", число {b}')
    
    # if 'j' in a or 'j' in b:
    #     a, b = complex(a), complex(b)
    # else: a, b = int(a), int(b)
    if 'j' in a: a = complex(a)
    else: a = int(a)
    if 'j' in b: b = complex(b)
    else: b = int(b)

    return a, b, operator

def set_data():
    pass

