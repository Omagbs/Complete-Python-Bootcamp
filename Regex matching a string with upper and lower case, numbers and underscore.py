"""
A  python program that print matches for a string that contains upper case, lower case, numbers and underscore
"""

import re

def matching_UPPER(text):
    pattern = "^[A-Z]*$"
    if re.search(pattern, text):
        print("Match found for UPPER")
    else:
        print("Match not found for UPPER!")

def matching_lower(text):
    pattern = "^[a-z]*$"
    if re.search(pattern, text):
        print("Match found for lower")
    else:
        print("Match not found for lower!")

def matching_number(text):
    pattern = "^[0-9]*$"
    if re.search(pattern, text):
        print("Match found for number")
    else:
        print("Match not found for number!")

def matching_All(text):
    pattern = "^[a-zA-Z0-9_]*$"
    if re.search(pattern, text):
        print("Match found for All")
    else:
        print("Match not found for All")

matching_lower("abc")
matching_lower("ABC")

matching_UPPER("ABC")
matching_UPPER("abc")

matching_number("019191")
matching_number("as0")

matching_All("Adsd8eje_")
matching_All("addsd?")