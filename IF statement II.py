#Code to check if a character is number, alphabet or space

ch = (input("Please enter the character: "))

if ch.isalpha():
    print("Your character is an Alphabet")
if ch.isnumeric():
    print("Your character is a number")
if ch.isspace():
    print("Your character is space")
