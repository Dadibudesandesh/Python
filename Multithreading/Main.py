import threading
import time

def print_numbers():
    for i in range(5):
        print("Number : ",i)
        time.sleep(1)
        print(threading.current_thread().name)

def print_letter():
    for letter in ['A','B','C','D','E']:
        print("Letter : ",letter)
        time.sleep(1)
        print(threading.current_thread().name)



# Create Threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)

# Start Threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()


print(threading.active_count())
print("Done")



def task():
    print(f"Running on thread: {threading.current_thread().name}")

for i in range(3):
    t=threading.Thread(target=task,name=f"Worker-{i+1}")
    t.start()
