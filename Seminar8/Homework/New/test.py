# {'1а': {'Иванов': 'хор', 'Петров': 'удо'}, '2а': {'Сергеев': 'отл'}}
# {'1а': {'Иванов': 'хор', 'Петров': 'отл'}, '2а': {'Сергеев': 'уд'}}
# Храним:
# 1а
# {'Иванов': 'хор', 'Петров': 'отл'}
# 2а
# {'Сергеев': 'уд'}

# После сплита(onstring):
# ['1а', "{'Иванов': 'хор', 'Петров': 'отл'}", '2а', "{'Сергеев': 'уд'}"]

# Как  собрать словарь?
# {'1а': {'Иванов': 'хор', 'Петров': 'отл'}, '2а': {'Сергеев': 'уд'}}

def receive_entry():
    with open(r'Seminar8/Homework/New/dict_students.txt', 'r', encoding="utf-8") as data:
        onstring = data.read().split("\n")[:-1]
        #onstring = data.read().split("\n")[:-1]
    db = dict()
    print(onstring)
    
    for i in range(0,len(onstring),2):
        key = onstring[i]
        value = eval(onstring[i+1])
        db[key] = value
            
    return db

print(receive_entry())
# print(max(receive_entry()))