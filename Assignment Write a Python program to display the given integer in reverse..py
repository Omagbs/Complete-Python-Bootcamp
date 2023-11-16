#Write a Python program to display the given integer in reverse.

num = int(input("Enter integer: "))

while num > 0:
    last_digit = num % 10
    print(last_digit, end="")
    num = num // 10
