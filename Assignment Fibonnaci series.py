# Assignment on a program to find the Nth term in a Fibonacci series using recursion

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


x = int(input("Enter the Nth term for the Fibonacci series: "))

if x % 10 == 2:
    print("The value for the", x, "nd term is", fibonacci(x))
elif x % 10 == 1:
    print("The value for the", x, "st term is", fibonacci(x))
elif x % 10 == 3:
    print("The value for the", x, "rd term is", fibonacci(x))
else:
    print("The value for the", x, "th term is", fibonacci(x))
