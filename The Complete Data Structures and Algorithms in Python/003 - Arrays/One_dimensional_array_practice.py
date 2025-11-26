import array
#1. Create an array and traverse.
my_array = array.array('i',[1,2,3,4,5,9,9])
print('Task 1')
for i in my_array:
    print(i)
print('-'*30)

#2. Access individul elements through indexes.
print('\nTask 2')
print(my_array[2])    
print('-'*30)

#3. Append any value to the array using append() method.
print('\nTask 3')
my_array.append(7) 
print(my_array)
print('-'*30) 
  
#4. Insert value in an array using insert() method.
print('\nTask 4')
my_array.insert(0,9)
print(my_array)
print('-'*30)

#5. Extend python array using extend() method.  
print('\nTask 5')
my_array1 = array.array('i',[10,11,12])
my_array.extend(my_array1)
print(my_array)
print('-'*30)

#6. Add items from list into array using fromlist() method. 
print('\nTask 6') 
my_list = [99,98,100]
my_array.fromlist(my_list)
print(my_array)
print('-'*30)

#7. Remove any array element using remove() method. 
print('\nTask 7') 
my_array.remove(100)
print(my_array)
print('-'*30)
 
#8. Remove last array element using pop() method.
print('\nTask 8')
my_array.pop(-1)
print(my_array)
print('-'*30) 
 
#9. Fetch any element through its index using index() method. 
print('\nTask 9') 
print(my_array.index(11))
print('-'*30) 

#10. Reverse a python array using reverse(). 
print('\nTask 10') 
my_array.reverse()
print(my_array)
print('-'*30) 

#11. Get array buffer information through buffer_info() method. 
print('\nTask 11')
print(my_array.buffer_info())
print('-'*30) 

#12. Check for number of occurences of an element using count() method. 
print('\nTask 12') 
print(my_array.count(9))
print('-'*30) 

#13. Covert array to string using tostring()(use tobytes because tostring was deprecated since Pythong 3.2) method.
print('\nTask 13') 
my_string_list = my_array.tobytes()
print(my_string_list)

print('-'*30)  

#14. Covert array to a python list with same elemenst using tolist() method.  
print('\nTask 14') 
print(my_array.tolist())
print('-'*30)

#15. Append a string to char array using fromstring() method.
print('\nTask 15') 
intArray = array.array('i')
intArray.frombytes(my_string_list)
print(intArray)
print('-'*30) 
 
#16. Slice elements from an array.
print('\nTask 16') 
#last element -1 it doesn`t show you the exact element on position/index 4 but in position/index 3
print(my_array[:4])
print('-'*30)  
 


