
#Middle Function
#Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

    #myList = [1, 2, 3, 4]
    #middle(myList)  # [2,3]
    
my_list =  [1, 2, 3, 4,5,6,7]  
    
def middle(arr):
    arr = sorted(arr) 
    return arr[1:-1] 

print(middle(my_list))