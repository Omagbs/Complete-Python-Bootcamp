# Calling a custom module I created

import MyModule2

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("The larger number is: ", MyModule2.islarger(x, y))
print("The lesser number is: ", MyModule2.isSmaller(x, y))
