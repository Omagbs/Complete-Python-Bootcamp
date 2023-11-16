#Cube and Square of a given number

x = int(input("Please enter your number: "))

def square(a):
    return(a**2)

def cube(a):
    return(a**3)

print("Square of the ", x, " is ", square(x))
print("Cube of the ", x, " is ", cube(x))