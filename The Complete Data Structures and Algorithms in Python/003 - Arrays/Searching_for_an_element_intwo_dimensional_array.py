import numpy as np

array_two_dimensional = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

print(array_two_dimensional)

def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == value:
                return print(f'Value {value} found in the index {i},{j}')
            
    return print('Value not found')           
            
            
            
searchTDArray(array_two_dimensional, 999)            
            