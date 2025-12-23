#  calculate sum of factorial upto n terms using function

def factorial(no):
    fact=1
    for i in range(1,no+1):
        fact*=i
    return fact

def sum_of_factorial(n):
    total=0
    for i in range(1,n+1):
        total+=factorial(i)
    return total

no=int(input("Enter number of terms : "))
if no<0:
    print("Please enter a positive number : ")
else:
    result=sum_of_factorial(no)
    print(f"Sum of Factorials upto {no} terms = {result}")
