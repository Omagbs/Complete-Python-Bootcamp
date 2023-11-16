# Python program to find the area of a triangle whose sides are given

a = int(input("Please enter the length of the first side of the triangle: "))
b = int(input("Please enter the length of the second side of the triangle: "))
c = int(input("Please enter the length of the third side of the triangle: "))

S = (a+b+c)/2

Area = (S * (S-a) * (S-b) * (S-c))**0.5
print("Area of the triangle is: ", Area)