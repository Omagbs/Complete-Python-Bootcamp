"""
Write a program to Reverse a List in Python.

Examples:

Input : list = [4, 5, 6, 7, 8, 9]

Output : [9, 8, 7, 6, 5, 4]
"""

txt = input("Use 'space' to separate the element. \nEnter element here: ")
list1 = txt.split()
new_txt = ""
for i in list1[::-1]:
    new_txt = new_txt + i + " "
print(new_txt.split())