# This code displays how files can be renamed and removed through pyhton IDE
# To rename, we have this syntax rename(Old_filename, New_filename)
# Also, you have to import the OS library

import os
# I ran this first
os.rename("File2.txt", "The Lord of the Rings.txt")
print("file has successfully been renamed")

# you can always change it back
#os.rename("The Lord of the Rings.txt", "File2.txt")
# print("file has successfully been renamed, again")

# Also, you can always delete a file using the remove operation
# its syntax is remove(filename). Don't  forget about importing your os module

# since I'm not using it, I better just delete it
os.remove("File3.txt")