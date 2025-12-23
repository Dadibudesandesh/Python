class Library:
    def __init__(self):
        print("Library calss")
    

class Teacher(Library):
    def __init__(self):
        super().__init__()
        print("Teacher Class")


class Student(Library):
    def __init__(self):
        super().__init__()
        print("Student Class")


class Book(Teacher,Student):
    def __init__(self):
        Teacher.__init__(self)
        Student.__init__(self)


book=Book()

