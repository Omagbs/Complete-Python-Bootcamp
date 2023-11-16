#a program to count the number of digits in a interger

x = int(input("Input your number here: "))
i = 0 #counter

while x>0:
    i = i + 1
    x = x//10

print(i)