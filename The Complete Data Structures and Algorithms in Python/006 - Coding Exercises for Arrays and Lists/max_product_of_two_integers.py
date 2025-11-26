# import numpy as np


# my_array = np.array([1,7,3,4,9,5])

# def max_product(arr):

#     result_list = np.array([])

#     for i in range(len(my_array)):
#         for j in range(len(my_array)):
#             if my_array[i] ==  my_array[j]:
#                 continue
                
#             else:
#                 result_list = np.append(result_list, my_array[i] * my_array[j] )
#     return max(result_list)

# print(max_product(my_array))



# import array
# my_array = array.array('i',[1,7,3,4,9,5])
# def max_product(arr):
#     result_list = array.array('i',[])
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i] ==  arr[j]:
#                 continue
#             else:
#                 result = arr[i] * arr[j]
#                 result_list.append(result)
#     return max(result_list)
            
    
# print(max_product(my_array))


import array
my_array = array.array('i',[1,7,3,4,9,5])
def max_product(arr):

    arr = sorted(arr)
    return arr[-1] * arr[-2]

print(max_product(my_array))