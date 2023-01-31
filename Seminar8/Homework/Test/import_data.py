import check as ch
import csv



def from_file():
    pass

def create_student():
    # pass
    surname = input("Введите фамилию ученика: ")
    # name = input("Введите имя ученика: ")
    # otch = input("Введите отчество ученика: ")
    # birth = input("Введите дату рождения ученика: ")
    tel = input("Введите телефон ученика: ")
    # adress = input("Введите адрес ученика: ")
    class_name = input("Введите наименование класса ученика: ")
    # global all_classes
    # if class_name not in all_classes:
    #     create_cl(class_name)
    global id_student
    # all_classes[class_name]=id_student
    # st_data = [surname, name, otch, birth, tel, adress, class_name]
    st_data = [surname, tel, class_name]
    # st_data = [surname, tel]
    global all_students
    all_students[id_student] = st_data
    print(all_students)
    ch.press_key()
    
    with open(r"Seminar8/Homework/dict_students.csv", 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        # for key, value in all_students.items():
        for key, value in all_students.items():
            writer.writerow([key, value])
        
    id_student += 1
    # for key in all_students:
    #     print(all_students[key])
    # print(all_classes)
    
    # with open(r"Seminar8/Homework/dict_classes.csv", 'w+', encoding="utf-8") as file:
    #     writer = csv.writer(file)
    #     for key, value in all_classes.items():
    #         writer.writerow([key, value])

    # with open(r"Seminar8/Homework/dict_classes.txt", 'a', encoding="utf-8") as file:
    #     file.write(all_classes)

def create_cl(name_class=False):
    # pass
    if not name_class:
        name_class = input("Введите номер класса: ")
        all_classes = name_class
    # print(all_classes[name_class])

def edit_student():
    pass
    # student_id = input("Введите id ученика: ")
    # surname = input("Введите фамилию ученика: ")
    # name = input("Введите имя ученика: ")
    # otch = input("Введите отчество ученика: ")
    # birth = input("Введите дату рождения ученика: ")
    # tel = input("Введите телефон ученика: ")
    # adress = input("Введите адрес ученика: ")
    # class_name = all_students[student_id][-1]
    # new_st_data = [surname, name, otch, birth, tel, adress, class_name]
    # all_students[student_id] = new_st_data

def delete_student():
    pass
    # student_id = int(input("Введите id студента."))
    # global all_classes
    # global all_students
    # all_classes[all_students[student_id][-1]].remove(student_id)
    # del all_students[student_id]

def change_class():
    pass
    # student_id = int(input("Введите id студента."))
    # old_class_number = all_students[student_id][-1]
    # new_class_number = input("Введите номер нового класса.")
    # global all_classes
    # global all_students
    # all_classes[old_class_number].remove(student_id)
    # all_classes[new_class_number].append(student_id)