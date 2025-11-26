my_dict = {'a': 5, 'b': 9, 'c': 2}


def highest_value(arr):
    max_value = max(my_dict.values())
    for i in arr:
        if arr[i] == max_value:
            return i
        
 
print(highest_value(my_dict))


#More efficient way
def max_value_key(arr):
    return max(arr, key=arr.get)


print(max_value_key(my_dict))