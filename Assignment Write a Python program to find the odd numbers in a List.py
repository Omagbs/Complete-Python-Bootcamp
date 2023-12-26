# Write a Python program to find the odd numbers in a List

# Create the list first
n = int(input("Enter the N number of elements on the list: "))
list_1 = []

# Take in elements into the list container
for i in range(0, n):
    x = int(input("Enter Element: "))
    list_1.append(x)

print(list_1)

# Odd number finder function

def isOdd(list):
    for i in range(len(list)):
        if (list[i] % 2) != 0:
            print("Element", list[i], "at index", i, "is an odd number on this list")

isOdd(list_1)