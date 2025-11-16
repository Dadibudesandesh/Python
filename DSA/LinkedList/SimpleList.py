class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
       
class LinkedList:
    def __init__(self):
        self.head=None
       
    def insert_at_pos(self,data,pos):
        newNode = Node(data) # create a new node of given data
        if pos<1:
            print("Invalid Position")
            return
        if pos==1:
            newNode.next=self.head
            self.head=newNode
            return
        temp=self.head
        count=1
        while temp and count<pos-1:
            temp=temp.next
            count+=1
            if temp is None:
                print("Position out of Bound")
                return
        newNode.next=temp.next
        temp.next=newNode

    def addition_of_nodes(self):
        temp=self.head
        sum=0
        while temp:
            sum+=temp.data
            temp=temp.next
        print("Sum of nodes is : ",sum)

    def insert_at_begin(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode

    def insert_at_end(self,data):
        newNode=Node(data)
        temp=self.head

        while temp.next!=None:
            temp=temp.next
        temp.next=newNode

    def delete_at_begin(self):
        self.head=self.head.next
    
    def delete_at_end(self):
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None

    def delete_at_pos(self,pos):
        if pos<1:
            print("Invalid Position")
            return
        if pos==1:
            self.head=None
            return
           
        temp=self.head
        count=1
        while temp and count<pos-1:
            temp=temp.next
            count+=1
           
            if temp is None:
                print("Position out of Bound")
                return
        temp.next=temp.next.next

    def display_list(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")
       
ll=LinkedList()
ll.insert_at_pos(10,1)
ll.insert_at_pos(20,2)
ll.insert_at_pos(30,3)


ll.insert_at_begin(60)
ll.insert_at_begin(70)
ll.insert_at_begin(90)

ll.insert_at_end(1)
ll.display_list()

ll.delete_at_begin()
ll.display_list()

ll.delete_at_end()

ll.display_list()

ll.delete_at_pos(3)
ll.display_list()

ll.addition_of_nodes()