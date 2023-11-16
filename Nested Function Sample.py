#illustration of Nested Function to find the square and the cube of a function

def square_n_cube(n):
    var = n
    def square(n):
        return n**2
    return square(var), n**3


x = int(input("Enter an integer: "))

print("The square and cube of the number is: ", square_n_cube(x))