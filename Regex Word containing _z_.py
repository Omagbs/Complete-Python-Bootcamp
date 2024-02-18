"""
A python program that prints matches if a given text has the letter "z" in it
"""

import re


def matching(text):
    pattern = '\w*z.\w*' # this pattern signifies z after a word or z before a word
    if re.search(pattern, text):
        print("match found")
    else:
        print("match not found")


text1 = "john"
text2 = "Jozn"
matching(text1)
matching(text2)
