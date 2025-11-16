# Stack using List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
top=None

def isEmpty():
    if top==None:
        return 1
    else:
        return 0

def push():
    global top
    data=input("Enter data to push : ")
    newNode=Node(data)
    newNode.next=top
    top=newNode
    print("Data pushed ")

def pop():
    global top
    if isEmpty():
        print("Stack Underflow! Nothing to pop")
    else:
        print(top.data," Poped")
        top=top.next

def peek():
    if isEmpty():
        print("Stack is empty")
    else:
        print("Top data : ",top.data)

def display():
    if isEmpty():
        print("Stack is empty")

    else:
        temp=top
        while temp:
            print(temp.data)
            temp=temp.next

while True:
    print("\n1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        push()
    elif ch == 2:
        pop()
    elif ch == 3:
        peek()
    elif ch == 4:
        display()
    elif ch == 5:
        print("Exiting…")
        break
    else:
        print("Invalid choice!")


