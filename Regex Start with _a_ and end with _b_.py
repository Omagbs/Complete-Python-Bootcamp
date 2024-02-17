"""
A python program to match a string that has an 'a' followed by anything, then ending with 'b'
 """

# import regular expression module
import re


# create a function to take in the text to find out if it meets the criteria or not
def matching(text):
    pattern = "a.*?b$"
    if re.search(pattern, text):
        print("Match found!")
    else:
        print("Match not found!")


str_1 = str(input("Enter the text here: "))
matching(str_1)
