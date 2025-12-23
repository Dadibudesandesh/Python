# Polymorphism with function and Objects

class Dog:
    def sound(self):
        print("Bark...!")

class Cat:
    def sound(self):
        print("Meow....!")


# Same function , works with any object having 'sound()' method
def make_sound(animal):
    animal.sound()

dog=Dog()
cat=Cat()

make_sound(dog)
make_sound(cat)