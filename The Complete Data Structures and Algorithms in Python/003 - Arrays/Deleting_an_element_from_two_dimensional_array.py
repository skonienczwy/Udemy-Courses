import numpy as np

array_two_dimensional = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(array_two_dimensional)
#the second argument is the index row or column, the below case axis 1 = column and 0 the first column to be deleted. Same works for rows.
new_array_two_dimensional = np.delete(array_two_dimensional, 0, axis=1)

print(new_array_two_dimensional)