#Front
#Write a method to return the value (not the node) at the HEAD of the list.  If the list is empy, return null.

#Remove Front
#Write a method to remove the head node and return the new list head node.  If the list is empty, return null.

#Add Front
#Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to teh new head node.

#Bonus
#Add Track
#Write a method that accepts a value and create a new node, assign it to the end of the list.


#Create node class then create list class

class Node:
    def __iniit__ (self, val):
        self.val = val
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def front(self):
        if self.head:
            return self.head.val
    

    def remove_front(self):
        if self.head:
            self.head = self.head.next  

    def add-front(self, val):
        new = Node(val)
        if not self.head:
            self.head = new
        else:
            new.next = self.head
            self.head = new
