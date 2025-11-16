max=5
queue=[0]*max
front=-1
rear=-1


def inqueue():
    global front,rear
    if rear==max-1:
        print("Queue is overflow !")
    else:
        data=int(input("Enter data to enqueue : "))
        if front==-1:
            front=0
        rear+=1
        queue[rear]=data
        print(data," Inserted")

def dequeue():
    global front,rear
    if front==-1 or front>rear:
        print("Queue is Empty")
    else:
        print("Dequeued : ",queue[front])
        front+=1
    
def peek():
     if front==-1 or front>rear:
        print("Queue is Empty")
     else:
         print("Front element : ",queue[front])

def display():
    if front==-1 or front>rear:
        print("Queue is Empty")
    else:
        for i in range(front,rear+1):
            print(queue[i])

inqueue()
inqueue()
inqueue()
display()
dequeue()
peek()



