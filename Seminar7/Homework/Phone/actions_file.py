def export_directory_1(): # экспорт справочника (элементы через Enter)
    with open(r"Seminar7/Homework/Phone/phone_directory.txt", 'r', encoding="utf-8") as file_dict:
        file_export = open("Seminar7/Homework/Phone/export_1.txt", 'w', encoding="utf-8")
        line_temp = file_dict.readline()
        while line_temp:
            lst_temp = line_temp.split()
            line = str(lst_temp[0] + '\n' + lst_temp[1] + '\n' + lst_temp[2] + '\n' + lst_temp[3] + '\n' + '\n')
            file_export.write(line)
            line_temp = file_dict.readline()
        file_export.close()

def export_directory_2(): # экспорт справочника (элементы через ***)
    with open(r"Seminar7/Homework/Phone/phone_directory.txt", 'r', encoding="utf-8") as file_dict:
        file_export = open("Seminar7/Homework/Phone/export_2.txt", 'w', encoding="utf-8")
        line_temp = file_dict.readline()
        while line_temp:
            lst_temp = line_temp.split()
            line = str(lst_temp[0] + ' *** ' + lst_temp[1] + ' *** ' + lst_temp[2] + ' *** ' + lst_temp[3] + '\n')
            file_export.write(line)
            line_temp = file_dict.readline()
        file_export.close()
 
def import_file():
    with open("Seminar7/Homework/Phone/import.txt", 'r', encoding="utf-8") as file_dict:
        line_temp = file_dict.readlines()
        str_imp_line = ''
        for i in range(len(line_temp)): str_imp_line += ' '.join(line_temp[i][:-1].split()) + '\n'
        with open("Seminar7/Homework/Phone/phone_directory.txt", 'a', encoding="utf-8") as dict_database:
            dict_database.write(str_imp_line)
