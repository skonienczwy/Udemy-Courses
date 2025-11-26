# Conditional Filter
# Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.

# Example:

# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
# filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0) 
# Output:

# {'b': 2, 'd': 4}


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 

def filter_dic(arr, condition):

    return {key : value for key, value in arr.items() if condition(key, value)}

#instead k I could use _ or _k that is a Python convention that means:
# “I’m required to take this argument, but I’m not going to use it.” 
#k is not being accessed when the function filter_dic is called below
print(filter_dic(my_dict, lambda k, v: v % 2 == 0))   


