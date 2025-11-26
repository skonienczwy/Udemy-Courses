from multiprocessing.reduction import duplicate


class Node:
    def __init__(self, value):
        self.value = value # Assigns the given value to the node
        self.next = None # Initialize the next attribute to null


#empty linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None # Initialize head as None
        self.tail = None # Initialize tail as None
        self.length = 0 #Define the length of the linked list
        
    #Print out Linked List    
    def __str__(self):
        temp_node = self.head # Start from the head of the list
        result = ''
        while temp_node is not None:
            result += str(temp_node.value) # Store the value in the current node
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next # Move to the next node
        return result   
      
    #Adding values to the end of the Linked List    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node #This connects the last node to the new one:
            self.tail = new_node
        self.length += 1
        
    #Adding values to the beginning  of the Linked List   
    def prepend(self, value):
        new_node = Node(value) # Create a new node 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head # Next for new node becomes the  current head
            self.head = new_node # Head now points to the new node
        self.length += 1
    
    #Insert method covers append/prepend but not replace them
    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head
        
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            
        elif index == 0:
            new_node.next = self.head # Next for new node becomes the  current head
            self.head = new_node # Head now points to the new node
        else:   
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    
    #traverse and print the Linked List
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
                
    def search(self, target):
        current_node = self.head        
        while current_node:
            if current_node.value == target:
                return True
            current_node = current_node.next
        return False    
    
    #Returns the node
    def get(self, index):
        #returns the last element of the Linked List
        if index == -1:
            return self.tail
    
        if index < -1 or index >= self.length:
            return None
        current_node = self.head   
        for _ in range(index):
            current_node = current_node.next
            
        return current_node
    #Update the value of the node           
    def set_value(self, index, value):
        current_node = self.head
        #alternative way is re-use get() method created previously instead the  for _
        current_node = self.get(index)        
        # for _ in range(index):
        #     current_node = current_node.next
        if current_node is not None:
            current_node.value = value 
            return True
        return False
    
    
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
        else:
            popped_node = self.tail
            current_node = self.head
            while current_node.next is not self.tail:
                current_node = current_node.next
            self.tail = current_node
            current_node.next = None
            self.length -= 1
        return popped_node
            
                
    def remove(self, index):
        if index >= self.length or index <= -1:
            return None        
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1 or index == -1:
            return self.pop() 
        else:            
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            
        self.length -= 1
        return popped_node
        
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
           
    def reverse(self):
        if self.length <= 1:
            return self
        
        previous_value = None
        current_node = self.head
        self.tail = self.head 
        
        while current_node:
            next_node = current_node.next
            current_node.next = previous_value
            previous_value = current_node
            current_node = next_node
            
        self.head = previous_value   
        return self      
            
    def middle(self):
        current_node = self.head
        if self.length == 0:
            return self
        middle_index = self.length // 2        
        for _ in range(middle_index):
            current_node = current_node.next
            
        return current_node.value
    
    
    def remove_duplicates(self):
        if not self.head:
            return None

        current = self.head
        
        while current:
            runner = current
            while runner.next:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
            
            current = current.next  # Move to next node
        
        # Update tail (in case last node was removed)
        self.tail = self.get(self.length - 1)
        return self

            
            
        
        
 
new_linked_list = SinglyLinkedList()
#Adding values in an empty and at the final of the linked list
new_linked_list.append(2)
new_linked_list.append(4)
new_linked_list.append(3)

# print(new_linked_list)    
#Adding values at the beginning of the linked list 
new_linked_list.prepend(1)
new_linked_list.insert(4,4)
new_linked_list.insert(5,2)
print(new_linked_list)
print(new_linked_list.remove_duplicates())

# new_linked_list.traverse()
# print(new_linked_list)  
# print(new_linked_list.search(20))

# print(new_linked_list)  
# print(new_linked_list.get(1))
# print(new_linked_list.set_value(1,6))
# print(new_linked_list) 
# print(new_linked_list.pop_first())
# print(new_linked_list) 
# print(new_linked_list.pop())
# print(new_linked_list) 
# print(new_linked_list.remove(0))
# print(new_linked_list) 
# print(new_linked_list.delete_all())
# print(new_linked_list)
# print(new_linked_list.reverse())
# print(new_linked_list.middle())