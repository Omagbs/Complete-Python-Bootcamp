#Factorial of a given number using For loop

x = int(input("Enter number: "))

if (x < 0):
    print("Enter positive number only or zero")
else:
    fact = 1
    for i in range(1, x+1):
        fact = fact * i
    print(fact, " is the factorial of ", x)
