# Elementwise Sum
# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

# Example

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)  # Expected output: (5, 7, 9)



tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
#zip() alone doesn`t show an output...it needs to be converted to a data structure
print('Use of zip() function')
print(tuple(zip(tuple1, tuple2)))
print('-'*30)

# #map iterates with 2 different tuples and sum is being called inside map to sum after the tuples are checked.
print('My function output:')
def tuple_elementwise_sum(tuple1, tuple2):
    if len(tuple1) == len(tuple2):
        return tuple(map(sum, zip(tuple1, tuple2)))       
    else:
        return 'It is not possible to proceed with the operation'
  
   
   

print(tuple_elementwise_sum(tuple1, tuple2))
print('-'*30)
# #another way to implement the same. Using lambda, zip is not necessary
print('Second approach with lambda output')
print(tuple(map(lambda x,y : x+y, tuple1,tuple2)))
print('-'*30)


