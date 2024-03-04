"""
This code illustrates the use of dictionary in python
"""

# An example of a dictionary:

# A dictionary has a key and value in key:value format

course = {"course": "python", "version": "3", "fee": 5000, "duration": "45 days"}
print(course)

# You can also print the value of a key
print(course["course"])
# Another example is to use the get() function
print(course.get("duration"))

# To add more key with value to your dictionary: (You simply just add a new key and assign a new value to it
course["student"] = "Toba"
print("After addition to the dictionary, we a have:")
print(course)

# You can also modify your dictionary: (You simply to just equate an existing key to a new values)
print("After modifying your dictionary:")
course["duration"] = "60 days"
print(course)

# To remove a key you use the pop() function
print("After removing a \"duration\" key from the dictionary")
course.pop("duration")
print(course)

# Another way of removing an item from the dictionary is to use the popitem() function. note that the popitem() removes
# the last item from the dictionary
print("After using popitem function to remove the last item from the dictionary:")
course.popitem()
print(course)

# Now for accessing dictionary

# using for loop:
for key, value in course.items():
    print(key, ":", value)
print("another way:")
# Another way:
for key in course:
    print(key, course[key])
# Again, another way
print("Another way again: ")

# prints all the keys
for key in course.keys():
    print("key: " + key)
# prints all the values
for value in course.values():
    print("Value:", value)

# Len, str, and types in dictionary
# len()
n = len(course)
print("Length of dictionary is:", n)

# str()
print("The components of the dictionary are:", str(course))

# type()
print("Type of passed object:", type(course))