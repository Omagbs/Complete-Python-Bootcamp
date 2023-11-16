#Find max number between two integers
def findMax(a, b):
    if a != b:
        if a > b:
            return a
        else:
            return b
    else:
        print("Error! They are equal")

def findMin(a, b):
    if a != b:
        if a > b:
            return b
        else:
            return a
    else:
        print("Error! They are equal")

x = int(input("Input integer: "))
y = int(input("Input second integer: "))

print("Max is: ", findMax(x, y))
print("Min is: ", findMin(x, y))
