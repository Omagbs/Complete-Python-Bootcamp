"""
A python program that print matches for a string that starts with an 'a' that is followed by three b's
"""


# import regular expression
import re

# create function for matching criteria
def matching(text):
    pattern = "ab{3}?"
    if re.search(pattern, text):
        print("print match found!")
    else:
        print("match not found!")

text = str(input("Enter text here: "))
matching(text)


