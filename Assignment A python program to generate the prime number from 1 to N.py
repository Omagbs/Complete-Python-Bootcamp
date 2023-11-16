# Assignment A python program to generate the prime number from 1 to N

N = int(input("Enter the value of N: ")) #Takes the limit from user

for num in range(1, N+1): # 1 to N
    if num > 1: #1 is not a prime number
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)


