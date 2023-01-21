# def log_in(first_value, second_value, operator):
#     with open('Seminar7/Calc/logging.txt', 'a') as data:
#         data.write(f'{first_value} {operator} {second_value}\n')
#     return first_value, second_value, operator

# def log_res(result):
#     with open('Seminar7/Calc/logging.txt', 'a') as data:
#         data.write(f'{result}\n')
#     return result

def log_all(text):
    with open('Seminar7/Calc/logging.txt', 'a', encoding='utf=8') as data:
        data.write(text + '\n')

def log_out():
    with open('Seminar7/Calc/logging.txt', encoding='utf=8') as data:
        print(*data.readlines())
