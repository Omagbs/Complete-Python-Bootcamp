# This code is to illustrate how list works in python
# It is a type of container in python that is mutable

# List can be indexed, the beginning of the index is 0
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("By indexing, I've printed the first element on the number list", num_list[0])

# List can also be sliced
print("Slicing from any point till the end", num_list[3:])
print("Starts from the beginning and slicing out any point not needed", num_list[:8])
print("Slicing out the precise part of the elements needed", num_list[3:7])
print("Reversing the entire list", num_list[::-1])

# elements can be modified inside a list
alpha_list = ["a", "b", "c", "d", "e", "f", "g", "i"]
print("Alpha list untouched:", alpha_list)
alpha_list[7] = "h"
print("overwriting i with h by indexing on alpha list:", alpha_list)

# elements can be appended to a list
alpha_list.append("i")
print("appended i to the list of alpha", alpha_list)

# elements can also be extended
alpha_list.extend(["j", "k", "l"])
print("extended the alpha list", alpha_list)

# insertion of a new member is also possible
alpha_list.insert(0, "A")
print("inserted A in the alphas list", alpha_list)

# pop is a function that can used in list
alpha_list.pop()  # this pops off the last element of the list
print("After popping the list:", alpha_list)
alpha_list.pop(0)  # pops off the specified index
print("After popping a specified index:", alpha_list)

# remove, unlike pop function, deletes the element itself with no need for indexing
alpha_list.remove("e")
print("After removing 'e' with the remove function:", alpha_list)

fib = [1, 1, 2, 3, 5, 8, 13, 21]
print("This is the fib list:", fib)
# you can also perform modal count in a list using the count function
print("the count function prints the number of occurences 1 makes on the list:", fib.count(1))

# index can also be obtained using the index function
print("obtaining the index of 'j' element using the index function:", alpha_list.index("j"))

# list can also be reversed using the reverse function
alpha_list.reverse()
print("Reversing the alpha list:", alpha_list)

# list can be sorted -- rearranged, greatest to smallest and vice
numbers = [2, 10, 3, 2, 6, 7, 9, 10]
print(numbers)
print("Sorts and prints without modyfing:", sorted(numbers))  # this sorts and prints without modifying
print("See, nothing's changed: ", numbers)
numbers.sort()
print("modified with sorting:", numbers)
print("reversing the order of sorting:", sorted(numbers, reverse=True))

# Finding the Min and Max of an element
print("Minimum is:", min(numbers), "Max is:", max(numbers))

