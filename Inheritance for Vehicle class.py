"""
This program illustrates inheritance with Super class and subclass. A bus object will inherit all the variables and
methods of the parent vehicle class and display it
"""


# Parent Class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


# Child class inheriting from Parent class
class Bus(Vehicle):
    # This is used to just create the class without creating any module or attribute
    pass


school_bus = Bus("Volvo", "240", "12")
print("The name of the Bus is:", school_bus.name)
print("The max speed of the bus is:", school_bus.max_speed)
print("The mileage of the bus is:", school_bus.mileage)
