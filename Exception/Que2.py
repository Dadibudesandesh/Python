# calculate factorial; using function

def fact(no):
    if no==0:
        return 1
    else: 
        return no*fact(no-1)

no=int(input("Enetr Number For Calculate Factorial : "))
print(fact(no))        