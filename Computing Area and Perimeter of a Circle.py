"""
This code illustrates th creation of a python class named Circle constructed by radius and method which
will compute the area of a circle and perimeter of the circle
"""

from math import pi


class Circle:
    # This constructor takes in the radius variable
    def __init__(self, r):
        self.radius = r

    def area_of_cir(self):
        return pi * self.radius ** 2

    def peri_of_cir(self):
        return 2 * pi * self.radius


rad = int(input("Enter the radius of the circle: "))

cir = Circle(rad)
print("The area of the circle is: ", cir.area_of_cir())
print("The perimeter of the circle is: ", cir.peri_of_cir())