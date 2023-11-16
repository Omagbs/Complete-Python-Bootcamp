#Using Lambda as a parameter for a function
def func(fn, n):
    return (fn(n))

twice = lambda x: x * 2
thrice = lambda x: x * 3

print(func(twice, 4))
print(func(thrice, 3))