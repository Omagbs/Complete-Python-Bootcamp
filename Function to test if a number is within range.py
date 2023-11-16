#using function to check if number is within a given range
def range_check(n):
    if n in range(3, 9):
        print("%s is in range"%str(n))
    else:
        print("The number is outside the given range.")

x = int(input("Number to check if in range: "))

range_check(x)
