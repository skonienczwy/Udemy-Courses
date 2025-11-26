
#Pairs
#Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

#Example
# pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']
# Note:
# 4+3 comes from second and third elements from the main list.
# 3+4 comes from third and seventh elements from the main list.

import array


n = 7
my_array= array.array('i',[2, 4, 3, 5, 6, -2, 4, 7, 8, 9])

def pairs(arr, n):
    pairs = list()

    for i in range(len(arr)):
        for j in range(i+1,len(arr)): # only j > i -> avoid reversed pairs
            if arr[i] + arr[j] == n:
                pairs.append(f'{arr[i]} + {arr[j]}')
                
    return pairs
   
   
   
print(pairs(my_array, n))
# pairs.append(f'{2} + {2}')            
# print(pairs)