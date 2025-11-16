arr=[1,2,3,4,5,2,3,6,4,2,1 ] # Simple array declaration 

# arr.append(6)
# arr.append(7)

# arr.extend([8,9,10]) # Add multiple elements 

# arr.insert(11,11) # Insert at specific position

# print(arr) # Accessing array

def delete_element_at_pos(pos):
    if pos<1 or pos>len(arr):
          print("Invalid Position....!")
    else:
        for i in range(pos-1,len(arr)-1):
             arr[i]=arr[i+1]
        arr.pop()

def update_element_at_pos(pos,data):
        for i in range(len(arr)):
            if pos<0:
                print("Invalid Position...!")
            elif i==pos-1:
                arr[i]=data

def display_arr():
        if len(arr)!=0:
            for i in arr:
                print(i,end=" ")
            print("")
        else:
             print("Array is empty")

def remove_duplicate_element():
    unique=[]
    for i in arr:
          if i not in unique:
               unique.append(i)
    print("Array after removing duplication : ",unique)

def sparse_matrix():
    matrix=[[0,0,3,0,4],
            [0,0,2,0,5],
            [0,0,6,0,6],
            ]

    rows,cols=len(matrix),len(matrix[0])
    sparse=[]

    for i in range(rows):
         for j in range(cols):
            if matrix[i][j]!=0:
             sparse.append([i,j,matrix[i][j]])
    
    print("Sparse matrix (Triplet Form)")
    for row in sparse:
         print(row)


def reverse_array():
     arr=[5,4,3,2,1]
     start,end=0,len(arr)-1

     print("Normal Array : ",arr)
     while start<end:
          arr[start]=arr[start]^arr[end]
          arr[end]=arr[start]^arr[end]
          arr[start]=arr[start]^arr[end]

          start+=1
          end-=1

     print("Reversed Array : ",arr)

def find_vowels():
     str="Sandesh Dadibude"
     count=0
     vowels="aeiou"
     avl=[]
     print("String is  : ",str)
     for ch in str.lower():
          if ch in vowels:
               count+=1
               avl.append(ch)

     print("Total Vowels are : ",count)
     print(" Vowels are : ",avl)


def insert_element_in_Array_At_position():
     arr=[1,2,3,4,5]
     item=int(input("Enter Element to insert : "))
     pos=int(input("Enter Position : "))

     if pos<1 or pos>len(arr)+1:
          print("Invalid Position...!")
     else:
          arr.append(0)
          for i in range(len(arr)-1,pos-1,-1):
               arr[i]=arr[i-1]
          arr[pos-1]=item
          print("Array After Insertion : ",arr)

     
def evaluate_polynomial(coef,x):
     if not coef:
          return 0
     result=coef[0]
     for c in coef[1:]:
          result = result * x + c
     return result

# display_arr()

# update_element_at_pos(1,0)

# display_arr()

# delete_element_at_pos(1)

# display_arr()

# remove_duplicate_element()

# display_arr()

# sparse_matrix()

# reverse_array()

# find_vowels()

# insert_element_in_Array_At_position()

coefficients=[2,-6,2,-1]
x0=3
print("P(3) = ",evaluate_polynomial(coefficients,x0))









