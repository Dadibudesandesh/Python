class Bird:
    def fly(self):
        print("Birds can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")


bird=Bird()
penguin=Penguin()

bird.fly()      # Bird Version
penguin.fly()   # Penguin Version
