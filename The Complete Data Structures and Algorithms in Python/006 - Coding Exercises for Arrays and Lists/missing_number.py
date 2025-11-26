# Write a function to find the missing number in a given integer array from 1 to N.
# The function takes two parameters:
#   1. The array of integers.
#   2. The number of elements that should be in the full sequence.
#
# Example:
#   If the array is [1, 2, 4, 6, 3] and the second parameter is 6,
#   the function should return 5 as the missing number.


import numpy as np
my_array = np.array([1,2,3,4,6,7,8,9,10,11,12,13])
val = 13

def missing_number(arr, n):
    sum1 = n * (n+1) //2
    sum2 = np.sum(arr)
    print(sum1-sum2)        

            
missing_number(my_array, val)
     



