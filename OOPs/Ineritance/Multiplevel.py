class GrandFather:
    def __init__(self):
        print("GrandFather Class")
    
class Parent(GrandFather):
    def __init__(self):
        super().__init__()
        print("Parent Class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Class")

child=Child()
