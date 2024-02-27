"""
This code illustrates a simple calculator that performs addition, subtraction, division, multiplication,
and square root
"""
while True:
    print("Choose the operation you want to perform")
    print("Enter 1 for Addition")
    print("Enter 2 for Subtraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division")
    print("Enter 5 for Square root")
    print("Enter 6 to Exit")

    i = int(input("Enter choice: "))

    if i == 1:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Addition of %d and %d is:" % (x, y), x + y)

    elif i == 2:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Subtraction of %d from %d is:" % (y, x), x - y)

    elif i == 3:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("%d multiplied by %d is:" % (x, y), x * y)

    elif i == 4:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("%d divided by %d is:" % (x, y), x / y)

    elif i == 5:
        x = int(input("Enter number: "))
        print("Square root of %d is:" % x, x ** 0.5)

    else:
        break
