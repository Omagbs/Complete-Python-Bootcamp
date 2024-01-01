# Finding the Min and Max in a list manually

L = [23, 34, 45, 44, 33, 43, 56, 78, 67, 57, 90]

Min_L = Max_L = L[0]

for item in L:
    if item > Max_L:
        Max_L = item
    elif item < Min_L:
        Min_L = item

print("Maximum in the list is:", Max_L)
print("Minimum in the list is:", Min_L)