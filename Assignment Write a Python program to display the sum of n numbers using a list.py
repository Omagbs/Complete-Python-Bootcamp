# Write a Python program to display the sum of n numbers using a list

n = int(input("Enter the N number of elements on the list: "))

list_1 = []

for i in range(0, n):
    x = int(input("Enter Element: "))
    list_1.append(x)

print("The list is:", list_1)
total = sum(list_1)
print("The sum is:", total)

