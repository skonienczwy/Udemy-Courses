my_dict = {'a': 1, 'b': 2, 'c': 3}



def reverse_key_values(arr):
    reversed_dict = {}
    for i in arr:    
        reversed_dict[arr[i]] = i
    return reversed_dict
print(my_dict)
print(reverse_key_values(my_dict))



#Different approach with dictionary comprehension

def reverse_dict(my_dict):
    return {v: k for k, v in my_dict.items()}



print(reverse_dict(my_dict))