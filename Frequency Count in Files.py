# This code illustrates a program that accepts filename as input
# from the user. Opens the file and counts the number of times a
# character appears

# User inputs the filename
filename = input("Enter the file name here: ")

with open(filename) as file:
    text = file.read()
    character = input("Enter the character you wish to count: ")
    count = 0
    for char in text:
        if char == character:
            count += 1

    print("Count is:", count)
file.close()