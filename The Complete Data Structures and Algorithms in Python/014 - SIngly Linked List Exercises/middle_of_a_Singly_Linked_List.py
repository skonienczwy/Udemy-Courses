
# Middle of a Singly Linked List
# Write a function to find and return the middle node of a singly linked list. If the list has an even number of nodes, return the second of the two middle nodes.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    
    def middle(self):
        if self.length == 0 :
            return self
            
        middle_index = self.length // 2
        current_node = self.head
        
        for _ in range(middle_index):
            current_node = current_node.next
            
        return current_node.value
        
        