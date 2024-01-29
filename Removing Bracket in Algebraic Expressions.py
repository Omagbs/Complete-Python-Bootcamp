# This code illustrates how bracket can be removed in an algebraic expression

def bracket_remover(str):
    new_str = ""
    for i in str:
        if i not in "()":
            new_str += i
    return new_str


txt = str(input("Enter algebraic expression: "))

print(bracket_remover(txt))
