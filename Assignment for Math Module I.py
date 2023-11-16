# Question One
# Calculate the square root of the sum of two numbers.
# Prompt the user to enter two numbers.
# Calculate the sum of the two numbers.
# Compute the square root of the sum using the math.sqrt() function.
# Display the square root of the sum.

from math import sqrt as sq

x = int(input("Enter first number here: "))
y = int(input("Enter second number here: "))

sum = lambda a, b: a + b

print("The square root of the sum is: ", sq(sum(x, y)))
