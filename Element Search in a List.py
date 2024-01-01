# Searching for an element in a list

L = [23, 34, 45, 44, 33, 43, 56, 78, 67, 57, 90]

key = int(input("Enter Number: "))
found = 0

for item in L:
    if item == key:
        found = 1
        break

if found == 0:
    print("Element not found")
else:
    print("Element found on the list \nThe index the element is:", L.index(item))
