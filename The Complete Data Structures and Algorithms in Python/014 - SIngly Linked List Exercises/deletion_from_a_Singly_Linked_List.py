# Deletion from a Singly Linked List
# Write a function to delete a node from a singly linked list and return deleted_node.
# The function should take the index(starting from 0) of the node to be deleted as a parameter.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        find_node = self.head
        for _ in range(index):
            find_node = find_node.next
        return find_node
    
    
    def remove(self , index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            delete_node = self.head            
                      
            if self.length == 1:
                self.head = None
                self.tail = None
        
            else:
                self.head = self.head.next
            delete_node.next = None
            
        else:    
            previous_node = self.get(index-1)
            delete_node = previous_node.next
            previous_node.next = delete_node.next        
            
            if index == self.length -1:
                self.tail = previous_node
            
            delete_node.next = None        

        self.length -= 1
        return delete_node


