#Program that displays sum of digits in number using while loop

num = int(input("Please input number: "))
sum = 0
while(num>0):
    last_digit = num % 10
    sum = sum + last_digit
    num = num // 10
print("the sum is: ", sum)