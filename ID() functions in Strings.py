# This code illustrate the use of ID function in strings to show the address of element

# Finding the ID of an element

a = 10
address_a = id(a)

b = 10
address_b = id(b)

if address_a == address_b:
    print("Same address:", address_a)
else:
    print("Different")

# Note: When the variables have same value or element, the address will be the same as seen above

print("..................")

# when the value of the variable is different, they'll have different address

a = 10
address_a = id(a)

b = 11
address_b = id(b)

if address_a == address_b:
    print("Same address:", address_a)
else:
    print("The have different address")
    print("Address for a:", address_a, "\nAddress for b:", address_b)

print("..................")

# This also applies to string, same string gives same address and different string gives different address

str_1 = "God is good"
address_str_1 = id(str_1)

str_2 = "God is good"
address_str_2 = id(str_2)

if address_str_1 == address_str_2:
    print("Same address:", address_str_1)
else:
    print("The have different address")
    print("Address for str_1:", address_str_1, "\nAddress for str_2:", address_str_2)

print("..................")

str_1 = ""
str_2 = "God is good"
address_str_2 = id(str_2)
str_1 += str_1 + str_2
address_str_1 = id(str_1)

if address_str_1 == address_str_2:
    print("Same address:", address_str_1)
else:
    print("The have different address")
    print("Address for str_1:", address_str_1, "\nAddress for str_2:", address_str_2)

print("..................")

str_1 = "God is good"
address_str_1 = id(str_1)

str_2 = "GOD is good"
address_str_2 = id(str_2)

if address_str_1 == address_str_2:
    print("Same address:", address_str_1)
else:
    print("The have different address")
    print("Address for str_1:", address_str_1, "\nAddress for str_2:", address_str_2)