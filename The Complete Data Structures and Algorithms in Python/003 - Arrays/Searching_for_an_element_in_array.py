import array

my_array = array.array('i',[1,2,3,4,5,6])


def linear_search(arr, target):
    for i in range(len(arr)):
        if my_array[i] == target:
            return i
    #-1 means the target was not find in the array    
    return -1



print(linear_search(my_array,7))