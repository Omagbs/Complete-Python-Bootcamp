#Calculate the area of traingle using Heron's Formula
#area = sqrt(S*(S-a)*(S-b)*(S-c))

a = float(input("Input first side of the Triangle: "))
b = float(input("Input second side of the Triangle: "))
c = float(input("Input third side of the Triangle: "))

S = (a+b+c)/2

Area = (S*(S-a)*(S-b)*(S-c))**0.5
print("Area of Triangle is: ", Area)