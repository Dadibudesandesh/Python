class GrandFather:
    def __init__(self):
        print("GrandFather Class")
    
class Parent():
    def __init__(self):
        print("Parent Class")

class Child(Parent,GrandFather):
    def __init__(self):
        GrandFather.__init__(self)
        Parent.__init__(self)
        print("Child Class")


child=Child()
