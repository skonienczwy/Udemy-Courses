# Common Keys
# Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

# Example:

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# merge_dicts(dict1, dict2)
# Output:

# {'a': 1, 'b': 5, 'c': 7, 'd': 5}

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}


def common_keys(arr1, arr2):
    for index, value in arr2.items():
        arr1[index] = arr1.get(index, 0) + value
    return arr1

print(common_keys(dict1, dict2))


