#Program to display multiplication table

num = int(input("Enter number here: "))
x = int(input("input the length of the table: "))

for i in range(1, x+1):
    print(num, " x ", i, " = ", num * i)

