#practising keyword argument

def display_info (name, age, salary):
    print("Name:", name)
    print("Age:", age)
    print("Salary:", salary)

n = "Batiste"
a = 30
s = 100000000

display_info(age = a, salary = s, name = n)