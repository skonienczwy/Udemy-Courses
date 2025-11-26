my_dict ={3:'Three', 5:'Five', 9:'Nine', 2:'Two', 1:'One', 4:'Four'}

print(3 in my_dict)
print('Three' in my_dict.values())

print('Three' not in my_dict.values())

print(len(my_dict))
#function returns True if all elements in the given iterable are truthy. If not, it returns False
print(all(my_dict))
my_dict2 = {3:'Three', 5:'Five', 9:'Nine', 2:'Two', 1:'One', False:'False'}
print(all(my_dict2))

#function returns True if any element of an iterable is True. If not, it returns False.
print(any(my_dict))

#sort the keys
print(sorted(my_dict))