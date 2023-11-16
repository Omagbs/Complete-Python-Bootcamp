#A program that checks if a character is alphabet or not

ch = (input("Please input character: "))

if((ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z")):
    print(ch, " is an alphabet")
else:
    print(ch, " is not an alphabet")