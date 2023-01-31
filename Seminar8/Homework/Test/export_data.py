import import_data as id
import check as ch

def to_console(dict_stud):
    ch.clear()
    print('<<< Просмотр >>>')
    for key in dict_stud:
        print(dict_stud[key])
    ch.press_key()
    # print(id.all_classes)
    # ch.press_key()


def to_file():
    pass