# This code illustrate working with strings and its fundamentals

# Printing every element in a string with its index

str1 = "Batman!"
index: int = 0

for i in str1:
    print(str1[index], "... Index is:", index)
    index += 1

# Create gap
print("\n")

# Printing all the element without its index
index = 0
for i in str1:
    print(str1[index])
    index += 1

# Create gap
print("\n")

str2 = "Hello"
str3 = "World!"
index = 0
for i in str2:
    print(str2[index])
    index += 1
index = 0
for i in str3:
    print(str3[index])
    index += 1

# Create gap
print("\n")

# Printing out an element via index
str4 = "I'm Batman"
i = 4
print(str4[i])

# Create gap
print("\n")

# Concatenating strings
str5 = "Rice "
str6 = "and "
str7 = "Beans"

str8 = str5 + str6 + str7
# or
str5 += str6 + str7
print(str8)
print(str5)

# Create gap
print("\n")

# Concatenate String and Integer
str9 = "Big "
var1 = 7

str10 = str9 + str(var1)
print(str10)