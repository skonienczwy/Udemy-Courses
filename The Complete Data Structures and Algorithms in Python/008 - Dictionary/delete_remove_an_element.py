my_dict = {'Name':'Edy', 'Age':26, 'City': 'Amsterdam', 'Education': 'Master'}

print(my_dict)

del my_dict['Age']

print(my_dict)

my_dict.pop('Educatio', None) #Optional value for default if doesn't find the value e.g.: my_dict.pop('Education', None)
print(my_dict)

my_dict.clear()
print(my_dict)