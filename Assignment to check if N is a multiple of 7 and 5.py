#a code to check if number is a multiple of 7 and 5

n = int(input("Input number: "))

if(n % 5 == 0 and n % 7 == 0):
    print(n, " is a multiple of 7 and 5")
else:
    print(n, " is not a multiple")