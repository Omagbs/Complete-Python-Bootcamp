# This code shows how to reverse a string

def revstring(str):
    newstr = ""
    i = len(str) - 1
    while i >= 0:
        newstr += str[i]
        i -= 1
    return newstr

str_in = str(input("Enter your string you wish to reverse here:"))
print("Your reversed string is:", revstring(str_in))