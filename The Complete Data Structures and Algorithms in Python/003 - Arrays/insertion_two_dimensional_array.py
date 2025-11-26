import numpy as np

twoDArray = np.array([[11, 15, 10, 6],[10, 14, 11, 5],[12, 17, 12, 8],[15, 18, 14, 9]])
print(twoDArray)
print('-'*35)


#adding column
#axis=0 is adding a row axis=1 is adding a column. The number zero is the postion/index of the values.
newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis=1)

print(newTwoDArray)
print('-'*35)

#adding row
newTwoDArray = np.insert(twoDArray, 3, [[9,9,3,4]], axis=0)
print(newTwoDArray)
print('-'*35)

#adding row at the final
newTwoDArray = np.append(twoDArray, [[5,5,5,5]], axis=0)
print(newTwoDArray)
print('-'*35)

#adding column at the final
newTwoDArray = np.append(twoDArray, [[5], [5], [5], [5]], axis=1)
print(newTwoDArray)
print('-'*35)







