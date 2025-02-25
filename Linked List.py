####Single Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
    
    ##Insert element at the beginning    
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
            
   ###print the linked list
    def listprint(self):
        itr = self.head
        while itr:
            print(itr.data, end= "-->")
            itr = itr.next
            
        print("None")
    
    ###Insert element at end    
    def insertAtEnd(self, data):
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data)
        
        

    ###Remove given element             
    def remove(self, data):
        itr = self.head
        while itr:
            if itr.data == data:
                self.head = itr.next
                return
            
            elif itr.next.data == data:
                itr.next = itr.next.next
                return
                
            else:
                itr = itr.next
                
        print("Element not found")
 
 ###search for given element       
    def search(self, data):
        itr = self.head
        while itr:
            if itr.data == data:
                return itr
            else:
                itr = itr.next
                
        print("Element not in the List")
        
#calculate lenght of linked list        
    def lenght(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count
            

          
ll = SLL()
ll.insertAtBegin(1)
ll.insertAtBegin(2)
ll.insertAtBegin(3)
ll.insertAtEnd(9)


ll.remove(3)
ll.search(9)
ll.lenght()
ll.listprint()
        
        
####Double linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def addAtEnd(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = new_node
        new_node.prev = itr
            
            
   ###print the doubly linked list
    def dllprint(self):
        itr = self.head
        while itr:
            print(itr.data, end= "-->")
            itr = itr.next
            
        print("None")
    
    
    ##insert at beginning        
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            
    def print_forward(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next
            
    def print_backward(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        while itr:
            print(itr.data) 
            itr = itr.prev       
                      
dll = DoublyLinkedList()
dll.addAtEnd(4)
dll.addAtEnd(6)
dll.dllprint()
dll.print_forward()
dll.print_backward()


##Join two linked lists
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedListJoin:
  def join_lists(head1, head2):
    curr1 = head1 
    curr2 = head2

    while curr1.next: 
      curr1 = curr1.next

    curr1.next = curr2

    return head1 


   ###print the linked list
  def listprint(self):
    itr = head1
    while itr:
      print(itr.data, end= "-->")
      itr = itr.next
            
    print("None")
        
        
# Create sample linked lists
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)

head2 = Node(4)
head2.next = Node(5)
head2.next.next = Node(6)


LLJ = LinkedListJoin()
joined = join_lists(head1, head2)
LLJ.listprint() 