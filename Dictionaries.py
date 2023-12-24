# Dictionaries are containers in pythons that can be immutable.
# They operate the use of a key Value
# It takes a format like this {Key:Value}

# Creating a dictionary
dict1 = {}
print(dict1)

# Another way to create dictionary
dict2 = dict()
print(dict2)

# Adding element in the dictionary with key and values
dict3 = {"x": 1, "y": 2, "z": 3}
print(dict3)

# You can only access the values in dictionaries with keys
print(dict3["y"])

# They can also be indexed.
print(dict3.get("z"))
# It prints none if it can find the key
print(dict3.get("f"))
# It prints the default assigned to it if it can't find the key
print(dict3.get("h", 99))

# They are also mutable
dict3["y"] = 1
dict3["x"] = 0
print(dict3)

