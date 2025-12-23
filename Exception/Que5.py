# Check palindrome or not 

def isPalindrome(num):
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num//=10
    
    print(rev)
    if rev==num:
        return True

    return False

number=int(input("Enter Number For check palindrome : "))
if isPalindrome(number):
    print(f"{number} is palindrome")
else:
    print(f"{number} is Not Palindrome")
    