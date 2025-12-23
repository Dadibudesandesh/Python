#  Reverse the number

def rev_num(num):
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num//=10
    return rev

num=int(input("Enter Number To reverse it : "))
print(f"The reverse of {num} is {rev_num(num)}")
 


















      





