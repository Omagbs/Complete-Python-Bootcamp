"""tuple_1 = (1, 2, 3)
list1 = [tuple_1]
print(list1) """

"""
Use lists and tuples to solve the problem.

Questions for this assignment
Given a list of tuples, Write a Python program to remove all the duplicated tuples from the given list.
Examples:
Input : [(1, 2), (5, 7), (3, 6), (1, 2)]
Output : [(1, 2), (5, 7), (3, 6)]

Input : [('a', 'z'), ('a', 'x'), ('z', 'x'), ('a', 'x'), ('z', 'x')]
Output : [('a', 'z'), ('a', 'x'), ('z', 'x')] 
"""


def removeDuplicates(lst):
    return [t for t in (set(tuple(i) for i in lst))]

lst = [(1, 2), (5, 7), (3, 6), (1, 2)]
print(removeDuplicates(lst))




