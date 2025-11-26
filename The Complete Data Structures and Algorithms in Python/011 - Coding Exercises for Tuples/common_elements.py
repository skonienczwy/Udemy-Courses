# Common Elements
# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

# Example

# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (4, 5, 6, 7, 8)
# output_tuple = common_elements(tuple1, tuple2)
# print(output_tuple)  # Expected output: (4, 5)




tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)



# def common_elements(tuple1, tuple2):
#     new_tuple = tuple1 + tuple2
#     temp = set()
#     for i in range(len(new_tuple)):
#         if new_tuple.count(new_tuple[i]) > 1:
#             temp.add(new_tuple[i])
#     # print(new_tuple.count(new_tuple[i]))
#     return tuple(temp)
# print(common_elements(tuple1, tuple2))

#Simple resolution

def common_elements(tuple1, tuple2):
    #& find the common elements between the two sets
    return tuple(set(tuple1) & set(tuple2))

print(common_elements(tuple1, tuple2))

