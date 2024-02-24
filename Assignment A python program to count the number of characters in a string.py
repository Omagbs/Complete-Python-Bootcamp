"""
Python program to count the number of characters (character frequency) in a string.
Using dictionaries
"""

def counting_char(str):
    freq = {}
    for i in str:
        freq[i] = freq.get(i, 0) + 1
    print(freq)


txt = str(input("enter text here:"))
counting_char(txt)
