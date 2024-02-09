# This code illustrates how to manipulate files via python, by reading, writing and appending.

# To write a into file or write and create a file which has not being created before
file = open("file.txt", "w")
file.write("I'm batman")
file.close()
print("Data has been written into the file")

# To modify or overwrite
file = open("file.txt", "w")
file.write("Bruce Wayne is my Secret Identity")
file.close()
print("Data has been overwritten into the file")

# To write multiply lines
list_1 = ["Hi I'm Bruce\n", "And I'm Batman\n", "Nice to meet you"]
file = open("file.txt", "w")
file.writelines(list_1)
file.close()
print("Multiple lines have been written")

# To append to a file
file = open("file.txt", "a")
file.write("\nAnd, I'm in love with CatWoman")
file.close()
print("Line has been appended")

print(".................................")
# To read a file
file = open("file.txt", "r")
#fileobj.read([count])
print(file.read(100))
file.close()
print("The file has been read")

# Note that trying to read a file that doesn't exist will lead to an error

print(".................................")
# To read the file line by line
print("Reading the file, line by line")
file = open("file.txt", "r")
print("First line: ", file.readline())
print("Second line: ", file.readline())
print("Third line: ", file.readline())
print("Fourth line: ", file.readline())
file.close()

print(".................................")
# To read all the lines once in form of a list, though
file = open("file.txt", "r")
print(file.readlines())
file.close()

# another way!
print(".................................")
# Turn your file into list
file = open("file.txt", "r")
print(list(file))
file.close()

print(".................................")
# Finally to print everything using For loop
file = open("file.txt", "r")
for line in file:
    print(line)
file.close()
