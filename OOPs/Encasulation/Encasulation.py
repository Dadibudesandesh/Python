
class Student:
    _id=0
    def __init__(self,name,age):
        self.name=name
        self.__age=age


    def show(self):
        print(f"Name : {self.name} , Age : {self.__age}")

    def get_age(self):
        return self.__age
    

    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Invalid Age!")

stud=Student("Sandesh",21)
stud.show()

print(stud.name)
print(stud.get_age())

stud.name="Kunal"
stud.set_age(23)

print(stud.name)
print(stud.get_age())

stud._id=10
print(stud._id)
    

        