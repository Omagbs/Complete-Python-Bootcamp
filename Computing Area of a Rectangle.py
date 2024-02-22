"""
This code illustrates th creation of a python class named Rectangle constructed by length and width and method which
will compute the area of a rectangle
"""


class Rectangle:
    # This constructor takes in the parameters of length and breadth
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    # method for area of the rectangle
    def area_of_rectangle(self):
        return self.length * self.breadth


x = int(input("Enter the length of the rectangle: "))
y = int(input("Enter the breadth of the rectangle: "))

rec = Rectangle(x, y)
print("The area of the Rectangle is: ", rec.area_of_rectangle())
