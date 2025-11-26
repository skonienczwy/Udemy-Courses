#Duplicate Number
#Write a function to remove the duplicate numbers on given integer array/list.

#Example

    #remove_duplicates([1, 1, 2, 2, 3, 4, 5])
    #Output : [1, 2, 3, 4, 5]
import array
my_array = array.array('i',[1, 1, 2, 2, 3, 4, 5]) 

def remove_duplicates(arr):     
    arr = set(arr)    
    return list(arr)

print(remove_duplicates(my_array))
