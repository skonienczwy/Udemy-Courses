my_dict = {'Name':'Edy', 'Age':26, 'City': 'Amsterdam', 'Education': 'Master'}
print(my_dict)


#copying a copy of the original dictionary
new_dict = my_dict.copy()
print(new_dict)
#create a dictionary from the given sequence of keys and values.
another_dict = dict.fromkeys([1,2,3],'Test')
print(another_dict)

#retun values from a key if the key exists,second param is incase the key is not present(it is optional)
print(my_dict.get('Name','Not Found'))
#method returns a view object that displays a list of dictionary's (key, value) tuple pairs
print(my_dict.items())

#retun keys from the dictionary 
print(my_dict.keys())

#remove last item from the dictionary and  it returns what was removed
print(my_dict.popitem())

#remove an item given the key, second parameter is optional in case the key is not found
print(my_dict.pop('Name', 'Key does not exist'))

#It returns a value from key if exists...otherwise it will create one
print(my_dict.setdefault('Education', 'High-School'))
print(my_dict)

#It returns the values(not include the keys) of the dictionary
print(my_dict.values())




newDict = {'a': 1, 'b': 2, 'c' : 3 }
#method updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs.
my_dict.update(newDict)
print(my_dict)

#delete all elements
my_dict.clear()
print(my_dict)