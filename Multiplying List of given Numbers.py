#function to multiply lists of given numbers

def multiply(nums):
    total = 1
    for i in (nums):
        total*=i
    return total

print(multiply((8, 2, 3, -1, 7)))
