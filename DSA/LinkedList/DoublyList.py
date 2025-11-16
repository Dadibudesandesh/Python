class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode

            
    def insert_at_end(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
            newNode.prev=temp
        
    def insert_at_pos(self,pos,data):
        newNode=Node(data)
        if pos<1:
            print("Invalid Position")
            return
        if pos==1:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
            return
        temp=self.head
        count=1
        while temp and count<pos-1:
            temp=temp.next
            count+=1
            if temp is None:
                print("Position Invalid")
                return
        newNode.next = temp.next
        newNode.prev = temp
        temp.next = newNode
        if newNode.next:
            newNode.next.prev = newNode


    def display_forward_list(self):
        temp=self.head
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")


    def display_backward_list(self):
        temp=self.head
        while temp.next!=None:
            temp=temp.next 
        while temp:
            print(temp.data,end="<->")
            temp=temp.prev
        print("None")
        

dll=DoublyLinkedList()
dll.insert_at_begin(10)
dll.insert_at_begin(20)
dll.insert_at_begin(30)
dll.insert_at_end(40)
dll.insert_at_pos(3,50)

dll.display_forward_list()
dll.display_backward_list()
