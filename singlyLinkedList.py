#creating node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#linked list and it's functionalities
class LinkedList:
    def __init__(self):
        self.head = None
    
#printing the linked list    
    def printf(self):
        n = self.head
        if n is None:
            print("Linked list is empty")
        else:
            while n is not None:
                print(n.data)
                n = n.next

#add element at the front    
    def pushfront(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

#add element at the end
    def pushback(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = newNode

#add after a given element
    def insertafter(self,data,k):
        newNode = Node(data)
        n = self.head
        while n is not None:
            if n.data is k:
                newNode.next = n.next
                n.next = newNode
                break
            n = n.next

#add before a given element
    def insertbefore(self,data,k):
        newNode = Node(data)
    #if k is the first element
        if self.head.data==k: 
            newNode.next = self.head 
            self.head = newNode 
    #otherwise
        else:
            n = self.head
            while n.next.data !=k:
                n = n.next
            newNode.next = n.next
            n.next = newNode

# delete first node
    def popfront(self):
        self.head = self.head.next

#delete last node
    def popback(self):
        n = self.head
        # if there is only one element in the linked list
        if n.next is None:
            self.head = None
        #otherwise    
        else:
            while n.next.next is not None:
                n = n.next
            n.next = None

#delete a given node
    def delete(self,data):
        n = self.head
        #if given node is the first node
        if n.data == data:
            self.head = self.head.next
        #otherwise
        else:
            while n.next.data is not data:
                n = n.next
            n.next = n.next.next


list1 = LinkedList()

# list1.pushfront("s")
# list1.pushback("f")
# list1.insertafter("z","f")
# list1.insertbefore("x","s")
# list1.popfront
# list1.popback()
# list1.delete('z')

list1.printf()