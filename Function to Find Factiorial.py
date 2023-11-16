#using function in python to find factorial of a given number

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

x = int(input("Please enter number here: "))
print("The factorial of", x, "is:", factorial(x))