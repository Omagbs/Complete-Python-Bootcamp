#using nested if statemtent to check which number is bigger

a = int(input("please input the first number: "))
b = int(input("please input the second number: "))

if a!=b:
    if a>b:
        print(a, " is bigger")
    else:
        print(b, "is bigger")
else:
    print(a, " is equal to ", b)