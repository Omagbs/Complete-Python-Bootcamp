# This code is the creation of a custom module called MyModule
# In Python, creation of module is possible, and it can contain several functions

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)
