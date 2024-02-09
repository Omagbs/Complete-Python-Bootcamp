# This code illustrate using the With keyword to manipulate files and also to split files

# To print everything using a the With keyword
with open("file.txt", "r") as file:
    print(file.read())
    file.close()

print("..............................")

# To spilt lines as sentences
with open("file.txt", "r") as file:
    line = file.readline()
    print(line)
    file.close()

# To split lines as words. It splits the words and prints it as in form of a list
with open("file.txt", "r") as file:
    line = file.readline()
    word = line.split()
    print(word)
    file.close()

# You can also add conditions or separators
with open("file.txt", "r") as file:
    line = file.readline()
    word = line.split("'") # This is the separator part, you can decide if you want to separate by using commas or any sign you wish
    print(word)
    file.close()