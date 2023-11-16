# Calculate the trigonometric functions of an angle. Prompt the user to enter an angle in degrees. Convert the angle
# to radians using the math.radians() function. Calculate the sine, cosine, and tangent of the angle using the
# math.sin(), math.cos(), and math.tan() functions respectively. Display the sine, cosine, and tangent of the angle.

import math

x = int(input("Enter angle in degrees here: "))

inRad = math.radians(x)

print("The sine of the angle is: ", math.sin(inRad))
print("The cosine of the angle is: ", math.cos(inRad))
print("The tangent of the angle is: ", math.tan(inRad))
