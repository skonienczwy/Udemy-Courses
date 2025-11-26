# Same Frequency
# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

# Example:

# list1 = [1, 2, 3, 2, 1]
# list2 = [3, 1, 2, 1, 3]
# check_same_frequency(list1, list2)
# Output:

# False



arr = [1, 2, 3, 2, 1]
arr1 = [3, 1, 2, 1, 3]

def check_same_frequency(lis1, list2):
    frequency = {}
    frequency2 = {}

    for i in lis1:
        frequency[i] = frequency.get(i, 0)+1
        
    for j in list2:
        frequency2[j] = frequency2.get(j, 0)+1
        
    return frequency == frequency2

print(check_same_frequency(arr, arr1))    


#alternative using Counter
from collections import Counter

def same_frequency(lis1, list2):
    return Counter(lis1) == Counter(list2)

print(same_frequency(arr, arr1))  