#Best Score
#Given a list, write a function to get first, second best scores from the list.

#List may contain duplicates.

#Example

    #myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
    #first_second(myList) # 90 87
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]    
def first_second(arr):
    arr = sorted(arr)
    return [arr[-1],arr[-2]]   

print(first_second(myList))