class Car:
    @staticmethod
    def start_engine(): #static method is a method that is not bound to an instance of the class.
        print("Engine Started...")

    @staticmethod
    def stop_engine():
        print("Engine Stopped...")

class ToyotaCar(Car):  # Inheritance used
    def __init__(self, brand): 
        self.brand = brand

class Fortuner(ToyotaCar): # Inheritance used
    def __init__(self, type):
        self.type = type

car1 = Fortuner("SUV")
car1.start_engine()

