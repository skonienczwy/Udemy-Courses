my_list = ['a', 'b', 'c', 'd', 'e' , 'f']

#slicing
print('Slicing a list')
print(my_list[1:3])
print('-'*30 + '\n')
#updating some elemnts defining the slice
print('Updating using slicing')
my_list[0:2] = ['x', 'y'] 
print(my_list[1:3])
print('-'*30 + '\n')

#deletion
print('Deleting using pop')
print(my_list)
my_list.pop(0)
print(my_list)
print('-'*30 + '\n')

print('Deleting using delete')
print(my_list)
del my_list[2]
print(my_list)
print('-'*30 + '\n')

print('Deleting using remove')
print(my_list)
my_list.remove('d')
print(my_list)
print('-'*30 + '\n')