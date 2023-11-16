#Write a Python program to print the numbers from a given number n till 0 using recursion

def print_all(n):
    print(n)
    if n==0:
        return 0
    else:
        return print_all n-1

x = int(input("Enter number:"))

print_all(x)