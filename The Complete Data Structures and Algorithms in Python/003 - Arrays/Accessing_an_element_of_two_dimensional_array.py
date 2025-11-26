import numpy as np
twoDArray = np.array([[11, 15, 10, 6],[10, 14, 11, 5],[12, 17, 12, 8],[15, 18, 14, 9]])

# print(twoDArray)
# print(twoDArray[0][3])

def access_element(array, row, column):
    if row < len(array) and  column < len(array[0]):
        return print(f'Value in Row {row} and column {column} is {array[row][column]}')
    else:
        return print('Invalid Index')



access_element(twoDArray,0,4)