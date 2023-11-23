# This code is to illustrate how list works in python
# It is a type of container in python that is mutable

mylist = [1, "a", 6.58]
print(mylist)

# the len function returns the number of items on the list
num_of_item = len(mylist)
print("Number of item on the list is:", num_of_item)

# Lists can also be concatenated
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
print("Concatenation of the list 1 and 2 is:", list_1 + list_2)

# List can also be repeated
repeat = list_1 * 3
print("Repeating List 1 thrice gives: ", repeat)

# Creation of empty list
list_3 = []
# Another way
list_4 = list()
print("Creation of empty list", list_3, list_4)
