"""
A program to create a vehicle class with max_speed and mileage instance attributes
"""


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


ModelX = Vehicle(240, 15)
print("The max speed of ModelX is:", ModelX.max_speed)
print("The mileage is:", ModelX.mileage)