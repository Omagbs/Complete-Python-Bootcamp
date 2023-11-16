# a Python program to find out the average of a set of integers

n = int(input("Enter the number of integers: "))
sum = 0
i = 1

while i <= n:
    x = int(input("input number: "))
    sum = sum + x

    i += 1
print("average of the given numbers is: ", sum/n)
