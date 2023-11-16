# Calculate the circumference and area of a circle.
# Prompt the user to enter the radius of a circle.
# Calculate the circumference of the circle using the formula 2 * math.pi * radius.
# Calculate the area of the circle using the formula math.pi * radius ** 2.
# Display the circumference and area of the circle.

from math import pi

r = int(input("Enter the radius of the circle here: "))

circumference = 2 * pi * r
area = pi * r**2

print("The area of the circle is:", area, ", while the circumference is:", circumference)