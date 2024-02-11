# This code illustrates the use of Regular Expression module and its built functions for manipulation of strings
# to using built in function for the Regular Expression, you have to import the re library

# using the match(pattern, string) The pattern is what is to be searched for in the string

import re

str_1 = "She sells sea shells on the sea shores"
pattern = "sea"

if re.match(pattern, str_1):
    # that is if this condition is true
    print("Match found")
else:
    print("Match not found")
# The result is match not found because when using the match function, it searches on the first part of the string
# Let's change the pattern to "She" to sea what happens
print("..............................................")
print("After changing pattern to 'She' from 'sea':")
pattern = "She"
if re.match(pattern, str_1):
    # that is if this condition is true
    print("Match found")
else:
    print("Match not found")

# Next function we have is the search(pattern, string). With this function,it searches the whole string for the pattern
print("..............................................")

pattern = "shells"
if re.search(pattern, str_1):
    print("Match found")
else:
    print("Match not found")

print("..............................................")
# Next we have the substitute function. its syntax is sub(pattern, repl, string, max=0)
# the pattern is the target, the repl is what you want to replace it with, string is where the target is located, max is
# how many targets you want to replace or substitute. Although the default is max = 0 -- which signifies all on the str
# My IDE might be different, but i don't need to use "max", i just have to write the integer like that otherwise it leads
# to error
pattern = "sea"
repl = "ocean"
replaced_str1 = re.sub(pattern, repl, str_1)
print(str_1)
print(replaced_str1)
print("\n")
# so lets say I only want to change just one "sea" to "ocean"
replaced_str1 = re.sub(pattern, repl, str_1, 1)
print(str_1)
print(replaced_str1)

print("..............................................")
# Lastly, we have the findall() function. the syntax is findall(pattern, input_str, flags = 0)
# This function finds not just an item but a particular pattern

# This pattern finds all the patterns or word beginning with alphabet (lower or upper case), having space behind it and
# begins with a digit
pattern = r"[a-zA-Z]+ +\d+"

# it gets stored in the matches variable in form of a list
matches = re.findall(pattern, "LXI 2013, VXI 2015, VDI 2014, Marthi Suzuki cars in Naij")

# prints it like it's not a list
for i in matches:
    print(i, end=" ")

