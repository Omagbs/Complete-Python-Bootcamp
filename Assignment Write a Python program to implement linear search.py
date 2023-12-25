# Write a Python program to implement linear search

# Create the list first
n = int(input("Enter the N number of elements on the list: "))
list_1 = []

# Take in elements into the list container
for i in range(0, n):
    x = int(input("Enter Element: "))
    list_1.append(x)

print(list_1)

# Take the key to search for
key = int(input("Enter Key to search for:"))

# Function for linear search
def LinearSearch(key, list):
    n = len(list) # Length of list

    for i in range(0, n):
        if list[i] == key:
            return "Element found at index: " + str(i)
    return "Element not found"


print(LinearSearch(key, list_1))
