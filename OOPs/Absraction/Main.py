from abc import ABC,abstractmethod

class Vehicale(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicale):
    def start_engine(self):
        print("Car Engine Started...!")

class Bike(Vehicale):
    def start_engine(self):
        print("Bike Engine Started....!")

# v=Vehicale()

c=Car()
b=Bike()

c.start_engine()
b.start_engine()




