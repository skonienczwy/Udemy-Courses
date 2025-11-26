import array

#Declaring an array of integers
my_array = array.array('i')
print(my_array)
#Declaring an array of integers and the elements
my_array2 = array.array('i',[1,2,3,4])
print(my_array2)

#Declaring array using numpy
import numpy as np

np_array = np.array([], dtype=int)
print(np_array)

np_array2 = np.array([1,2,3,4])
print(np_array2)
 