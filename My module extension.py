# This program is to call my module

import MyModule

x = int(input("Enter the number you wish to find its  factorial: "))
y = int(input("Enter the nth term you wish to find in the fibonacci series:"))

print("The factorial of", x, " is: ", MyModule.fact(x))
print("The", y, "th term of the fibonacci series is: ", MyModule.fib(y))
