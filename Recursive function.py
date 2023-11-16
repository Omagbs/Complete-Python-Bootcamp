#using recursive function to find the factorial of a number

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)

x = int(input("Enter number: "))

print("Factorial of", x, "is:", fact(x))