# Stack using array

size=int(input("Enter size of stack : "))
stack=[0]*size
top=-1

def isfull():
    if(top==size-1):
        return 1
    else:
        return 0

def isempty():
    if(top==-1):
        return 1
    else:
        return 0

def push(data):
    global top
    if isfull()!=1:
        top+=1
        stack[top]=data
    else:
        print("Stack is full")
    
def pop():
    global top
    if(isempty()!=1):
        ele=stack[top]
        top-=1
        print("Poped element : ",ele)
    
def peek():
    print("Top element :",stack[top])

def display():
    global top
    if isempty():
        print("Stack is empty")
    else:
        for i in range(top+1):
            print(stack[i])

push(10)
push(20)
push(30)
push(40)
push(50)
display()
pop()
display()
peek()






