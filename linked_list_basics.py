"""class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
Node1 = Node(5)
Node2 = Node(6)
print(Node1.data)
"""





"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode
    def delete_begin(self,data):
        self.head = self.head.next
    def delete_end(self,data):
        if self.head is not None:
            if self.head.next is None:
                self.head = None

                
    def display(self):
        if self.head is None:
            return
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
linkedlist_1 = linkedlist()
linkedlist_1.insert(5)
linkedlist_1.insert(6)
linkedlist_1.insert(7)
linkedlist_1.insert(8)
linkedlist_1.insert(9)
linkedlist_1.delete_begin(9)
linkedlist_1.display()
"""




class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_begin(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            return
        self.head.prev = newNode
        newNode.next= self.head
        self.head = newNode
    def insert_end(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            return
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        
    def delete_begin(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head== self.tail :
            self.head = self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None
    def delete_end(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail =None
            return
        
        self.tail = self.tail.prev
        self.tail.next = None
    def display(self):
        if self.head is None:
            return
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
linkedlist_1 = linkedlist()
linkedlist_1.insert_begin(5)
linkedlist_1.insert_begin(6)
linkedlist_1.insert_begin(7)
linkedlist_1.insert_begin(8)
linkedlist_1.insert_begin(9)
linkedlist_1.insert_end(4)
linkedlist_1.insert_end(3)
linkedlist_1.delete_begin()
linkedlist_1.delete_begin()
linkedlist_1.delete_end()
linkedlist_1.display()




