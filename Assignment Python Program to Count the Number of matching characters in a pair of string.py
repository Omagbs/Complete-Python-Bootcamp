# A Python Program to Count the Number of matching characters in a pair of string
# Given a pair of non-empty strings. Count the number of matching characters in those strings (consider the single count for the character which have duplicates in the strings).

# Examples:

# Input : str1 = 'abcdef'

#        str2 = 'defghia'

# Output : 4

# (i.e. matching characters :- a, d, e, f)

txt_1 = str(input("Enter the first string: "))
txt_2 = str(input("Enter the second string: "))


def str_counter(str1, str2):
    # remove duplicates
    new_str1 = set(str1)
    new_str2 = set(str2)

    # intersection picks similar character or element
    matched = new_str1 & new_str2
    # count the number of similar element
    count = len(matched)

    return count

print("Number of Matching Characters: ", str_counter(txt_1,txt_2))
