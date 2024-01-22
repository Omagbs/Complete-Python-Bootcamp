# This code illustrates the built in function for strings

# To find the length of a string, the len() function is used

str1 = "Amazing Spider Man"
print("The length of the string \"" + str1 + "\" is:", len(str1))

# To indicate gap
print("................")

# To check if a string is alphabet or number with isalnum()
str2 = "1234"
str3 = "abcd3"
print(str2.isalnum())
print(str3.isalnum())

# To indicate gap
print("................")

# To check if a string is alphabet or not with is alpha()
print(str2.isalpha())
str2 = "ABCD"
print(str2.isalpha())

# To indicate gap
print("................")

# To check if a string is digit or not

str2 = "1234"
print(str2.isdigit())
print(str3.isdigit())

# To indicate gap
print("................")

# To check if a string is in lower case using islower()
print(str3.islower())
print(str2.islower())

# To indicate gap
print("................")

# To check if a string is in upper case using isupper()
str1 = "BATMAN"
print(str1.isupper())
print(str3.isupper())

# To indicate gap
print("................")

# To check if a string has white space ONLY using isspace()
print(str1.isspace())
str2 = "         "
print(str2.isspace())

# To indicate gap
print("................")

# To capitilize the first word in a string using capatilize()
str3 = "god is good"
print(str3.capitalize())

# To indicate gap
print("................")

# To change the string to lower case lower()
str1 = "BATMAN"
print(str1.lower())

# To indicate gap
print("................")

# To change the entire string to upper case using upper()
print(str1.upper())

# To indicate gap
print("................")

# To remove white spaces from the before and after the string
str3 = "        Your excellency sir          "
print(str3.strip())

# To indicate gap
print("................")

# To remove white spaces from the before string
str3 = "        Your excellency sir          "
print(str3.lstrip())

# To indicate gap
print("................")

# To remove white spaces from the after a string
str3 = "        Your excellency sir          "
print(str3.rstrip())