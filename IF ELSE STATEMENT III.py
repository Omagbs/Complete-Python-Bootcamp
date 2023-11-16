###A program to determine if a year is a leap year or not. A leap year should be divisible by 4. Should not be divisible by 100. and should be divisble by 400####

year = int(input("Please input the year: "))

if(year % 4 == 0 or year % 400 == 0) and (year % 100 != 0):
    print(year, " is a leap year")
else:
    print(year, " is not a leap year")