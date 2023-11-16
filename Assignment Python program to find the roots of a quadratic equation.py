#Python program to find the roots of a quadratic equation

#a is the coefficient of x^2
#b is the coefficient of x
#c is the constant

a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

root_1 = (-b + (b**2 - 4 * a * c) ** 0.5) / 2 * a
root_2 = (-b - (b**2 - 4 * a * c) ** 0.5) / 2 * a

print("Root 1: ", root_1)
print("Root 2: ", root_2)