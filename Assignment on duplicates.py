"""
Remove adjacent duplicate characters from a string
Given a string, remove adjacent duplicates characters from it. In other words, remove all consecutive
same characters except one.

For example,

Input:  AABBBCDDD
Output: ABCD
"""

txt = input("Enter string here: ")
new_txt = ""
for char in txt:
    if char in new_txt:
        pass
    else:
        new_txt += char

print(new_txt)

# or
stack = []


def duplicate_removal(str1):
    for char in str1:
        if char not in stack:
            stack.append(char)
    print(''.join(stack))


duplicate_removal("AAAABBBBBB")


# lecturers solution

def removeDuplicates(s):
    chars = []
    prev = None
    for c in s:
        if prev != c:
            chars.append(c)
            prev = c
    return ''.join(chars)


if __name__ == '__main__':
    s = 'AAABBCDDD'
    print(removeDuplicates(s))
