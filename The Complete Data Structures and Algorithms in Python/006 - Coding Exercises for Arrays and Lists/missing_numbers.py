def missing_numbers(arr, n):
    """
    Find all missing numbers in a sequence from 1 to n.
    
    Parameters:
        arr (list): Input list with some numbers missing
        n (int): Total numbers expected in the full sequence (1 to n)
    
    Returns:
        list: Sorted list of missing numbers
    """
    # Create a set of all numbers from 1 to n
    full_set = set(range(1, n+1))
    
    # Convert input list to set
    arr_set = set(arr)
    
    # Difference gives missing numbers
    missing = sorted(list(full_set - arr_set))
    
    return missing

# Example usage
my_array = [1, 2, 4, 6, 7,10]
n = 10
print(missing_numbers(my_array, n))

