# Write a Python program to find the odd numbers in a List

def isOdd(list):
    for i in (0, len(list)):
        if list[i]%2 != 0:
            print("Odd number ", list[i], "found at index: ", i)
