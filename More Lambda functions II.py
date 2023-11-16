# A code to illustrate Lambda functions
# This program will compare the smaller value of the differences of the two integers and the summation of the same numbers

def smaller(a, b):
    if a < b:
        return a
    else:
        return b


x = int(input("Enter first number here: "))
y = int(input("Enter second number here: "))

sum = lambda a, b: a + b
diff = lambda a, b: a - b

print("The sum is:", sum(x, y), "\n" "The difference is:", diff(x, y), "\n" "The smaller value between the "
                                                                         "difference and the  sum of the given "
                                                                         "integers is: ", smaller(sum(x, y), diff(x,
                                                                                                                  y)))
