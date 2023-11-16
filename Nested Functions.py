#illustration of how nested function works in python

def outer_func():
    var = 100
    def inner_func():
        var = 50
        print("Inner Function's var is", var)
    inner_func()
    print("Outter function's var is: ", var)

outer_func()