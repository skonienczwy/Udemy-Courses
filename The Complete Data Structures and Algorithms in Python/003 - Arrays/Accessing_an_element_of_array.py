import array

my_array2 = array.array('i',[1,2,3,4,5,6])

def accessElement(array, n):
    if n >= len(array):
        print('Element does not exist.')
    else:
        print(array[n])

accessElement(my_array2,6)