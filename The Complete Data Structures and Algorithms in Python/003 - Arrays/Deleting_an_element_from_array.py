import array

my_array = array.array('i',[1,2,3,4,5,6])

def removingElement (arr, element):
    #remove find the element you want to remove and pop find the index you want to remove
    arr.remove(element)
    return arr

# my_array.pop(0)

print(removingElement(my_array,3))
