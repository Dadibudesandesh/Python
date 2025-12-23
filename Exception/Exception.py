def divide_number(a,b):
    try:
        result=a/b
    except Exception as e:
        print(e)
    else:
        print( result)
    finally:
        print("Finally block called")

divide_number(10,2)
divide_number(10,0)
# print()
