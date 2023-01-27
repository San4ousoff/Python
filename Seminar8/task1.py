my_tuple = (1,2,3,4,5)
my_list = [5,7,8,9,0]
my_tuple_new = (11,22,33)
new_list = []

new_list.extend(my_tuple)
print(new_list)

new_list += my_list
print(new_list)

new_list += 'wetrergsdgsdghsdf'
print(new_list)

new_list.append(my_tuple)
print(new_list)
