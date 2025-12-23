# User Defined exception

class AgeNotWithinRangeException(Exception):
    def __init__(self, message="Age is not between 15-21"):
        super().__init__(message)

class NameNotValidException(Exception):
    def __init__(self, message="Name contains Characters"):
        super().__init__(message)

class Student:
    def __init__(self,roll_no,name,age,course):
        if not (15<=age<=21):
            raise AgeNotWithinRangeException()
        if not name.replace(" ","").isalpha():
            raise NameNotValidException()
        
        self.roll_no=roll_no
        self.name=name
        self.age=age
        self.course=course

    def dispaly(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Course : ",self.course)
        print("Roll No : ",self.roll_no)


try:
    print("Creating Valid Student : ")
    stu1=Student(1,"Sandesh",21,"MCA")
    stu1.dispaly()
    print("Creating Student  Invalid : ")
    stu2=Student(2,"Kunal",23,"MCA")
    stu2.dispaly()
except AgeNotWithinRangeException as e:
    print(e)
except NameNotValidException as e:
    print(e)