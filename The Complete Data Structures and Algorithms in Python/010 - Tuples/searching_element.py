new_Tuple = ('a','b','c','d','e')

print('a' in new_Tuple)

#returns the index where the value is
print(new_Tuple.index('c'))

def searchTuple(my_tuple, element):
    for i in range(len(my_tuple)):
        if my_tuple[i] == element:
            return f"Element {element} is in index {i}"
    return f'Element {element} not found'    
        
        
print(searchTuple(new_Tuple, 'e'))