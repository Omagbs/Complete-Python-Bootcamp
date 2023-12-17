# This code is to illustrate how list works in python
# It is a type of container in python that is mutable

# Some built in function of list containers
list_1 = [10, 20, 30, 40, 50, 50, 50, 60, 70, 80, 90, 100]
print("Original list is:", list_1)

# To find the index of an element
print("The index of 20 is", list_1.index(20))

# To find out the frequency of an element in a list
print("The frequency of 50 on the list is", list_1.count(50))

# To add an element to the list
list_1.append(110)
print("after appending 110 to the list:", list_1)

# To remove an element from the list
list_1.remove(50)
print("after removing 50 from the list:", list_1)