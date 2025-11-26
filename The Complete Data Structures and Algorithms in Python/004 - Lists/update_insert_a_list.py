my_list = [1,2,3,4,5,6,7]

print(my_list)
my_list[2] = 'xuxu'
print(my_list)


#Insert an element to the beginning of the list
my_list.insert(0,'Test')
print(my_list)
print('-'*30)

#Insert an element to the any given place in the list
my_list.insert(5,'Testando ')
print(my_list)
print('-'*30)
#Insert an element to the end of the list
my_list.append(69)
print(my_list)
print('-'*30)
#Insert another list to the list. Obs: It is extending to the current list, not inserting a list inside the list
new_list = [99,98]
my_list.extend(new_list)
print(my_list)
print('-'*30)


