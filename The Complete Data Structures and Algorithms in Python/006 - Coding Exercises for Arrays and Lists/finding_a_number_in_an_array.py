import numpy as np

my_array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
n = 1

def finding_a_number(arr, n):
    for i in range(len(my_array)):
        if my_array[i] == n:
            return print(f'Number {n} is in the array on position {i}')
            
            
finding_a_number(my_array, n)
# print(21 in my_array)