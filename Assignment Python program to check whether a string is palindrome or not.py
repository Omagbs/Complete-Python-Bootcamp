# Write a Python program to check whether a string is palindrome or not

# Palindrome means a word or phrase that reads the same backward as forward
# An example of a Palindrome is PAP, because turning the word backwards give pap

# Code

# Takes in the input text from the User
txt = str(input("Enter your text here: "))

# Function to reverse the string
def reversal(str_in):
    # New string variable for storing the reversed string
    new_txt = ""
    # To iterate in reverse
    for i in range((len(str_in) - 1), -1, -1):
        # Store each element in reverse order in the new string variable
        new_txt += str_in[i]
    return new_txt

# Function to check if the string is Palindrome or not
def isPalindrome(str_in, new_str):
    # convert both strings to low case since Palindrome is supposed to be case insensitive
    lowcase_str_in = str_in.lower()
    lowcase_new_str = new_str.lower()
    # compare each elements
    for i in range(0, len(str_in) + 1):
        # return negative if it's not Palindrome
        if lowcase_new_str[i] != lowcase_str_in[i]:
            return -1
        # return +ve if palindrome
        else:
            return 1


print("Reversed text is:", reversal(txt))

# interprete the function and print result
palindrome = isPalindrome(txt, reversal(txt))
if palindrome == 1:
    print("Text is Palindrome")
else:
    print("Text is not Palindrome")
