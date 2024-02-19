"""
A Class is a blueprint of an object
The contain attributes and functions

An example:
Rectangle -- Class
Width, height, and colour -- Attributes
Area() -- Function

This code illustrates the use of a class in python
"""


class Maths:
    def subtract(self, i, j):
        return i - j

    def add(self, x, y):
        return x + y


# creating object

m = Maths()
print(m.add(3, 5))
print(m.subtract(5, 3))
