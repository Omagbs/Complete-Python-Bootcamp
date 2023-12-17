# This code is to illustrate how list works in python
# It is a type of container in python that is mutable

# more built in function of list containers

# You can store multiple data types in a list

list_2 = [1, "Boy", "Cow", 2.34, 3]
print(list_2)

# you can also create multidimensional list
list_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# This is a 3x3 matrix
# [0][0] [ROWS][COLUMNS]

print("First element is:", list_2[0][0])
print("Last element is:", list_2[2][2])

# Nested list: List within a list

list_3 = [[1, 2, [3, 4]]]
print(list_3)