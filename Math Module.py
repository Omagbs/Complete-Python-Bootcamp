# This program illustrates the use of math Module

from math import pi  # This line of code calls the function of pi and doesn't call the whole math module
from math import \
    pow  # This line of code calls the function for power. The first index takes the number and the second index
# takes the value for which power it is to be raised


def area_of_circle(r):
    return pi * pow(r, 2)


def circumference(r):
    return 2 * pi * r


radius = int(input("Enter the Radius of the Circle: "))

print("The area of the circle is ", area_of_circle(radius))
print("The circumference of the circle is ", circumference(radius))
