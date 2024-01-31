# a python program to Remove all duplicates from a given string.

txt = str(input("Enter text: "))

print("".join(dict.fromkeys(txt)))

#or

t = ""
for i in txt:
    if i in t:
        pass
    else:
        t = t + i
print(t)