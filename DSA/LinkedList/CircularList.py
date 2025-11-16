class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_first(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
            self.head.next=self.head

    def insert_at_end(self,data):
        newNode=Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newNode
        newNode.next=self.head

    def insert_at_pos(self,pos,data):
        newNode=Node(data)
        temp=self.head
        count=1

        while temp.next!=None and count>pos-1:
            temp=temp.next
            count+=1
            if temp is None:
                print("Position Out Of Bound")
        
        newNode.next=temp.next
        temp.next=newNode
        

    
            

