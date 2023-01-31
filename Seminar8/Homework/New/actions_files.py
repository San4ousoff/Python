# Запись словаря в файл
# Получение данных из файла 

def add_entry(db):
    with open('Seminar8/Homework/New/dict_students.txt', 'w', encoding = 'utf-8') as file:
        for key, value in db.items():
            file.write(f'{key}\n{value}\n')
    
def receive_entry():
    with open(r'Seminar8/Homework/New/dict_students.txt', 'r', encoding="utf-8") as data:
        onstring = data.read().split("\n")[:-1]
    db = dict()
    for i in range(0,len(onstring),2):
        key = onstring[i]
        value = eval(onstring[i+1])
        db[key] = value
    return db
