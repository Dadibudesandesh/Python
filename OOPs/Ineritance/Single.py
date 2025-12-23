class Perent:
    def __init__(self):
        print("Perent class")

class Child(Perent):
    def __init__(self):
        super().__init__()
        print("Child Class")

class Main:
    ch=Child()