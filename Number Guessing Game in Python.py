"""
This code illustrates Number Guessing Game in Python
"""

import random

print("Hi Friend, welcome to this python guessing game!\nYou have seven tries to guess the number"
      "\nYou should specify the range by inputting lower bound and upper bound\nTha is all for now, Good luck Champ!\n")
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

random_number = random.randint(lower_bound, upper_bound)

counter = 1

while counter <= 7:
    x = int(input("Enter your number to see if matches: "))
    if x > random_number:
        if counter == 7:
            break
        elif counter == 1:
            print("you have 6 tries left")
        elif counter == 2:
            print("You have 5 tries left")
        elif counter == 3:
            print("you have 4 tries left")
        elif counter == 4:
            print("You have 3 tries left")
        elif counter == 5:
            print("you have 2 tries left")
        elif counter == 6:
            print("You have 1 try left")
        counter += 1
        print("Try again! You guessed high!")
    elif x < random_number:
        if counter == 7:
            break
        elif counter == 1:
            print("you have 6 tries left")
        elif counter == 2:
            print("You have 5 tries left")
        elif counter == 3:
            print("you have 4 tries left")
        elif counter == 4:
            print("You have 3 tries left")
        elif counter == 5:
            print("you have 2 tries left")
        elif counter == 6:
            print("You have 1 try left")
        counter += 1
        print("Try again! You guessed low!")
    elif x == random_number:
        print("Congratulations Buddy, You did it!!! How did you know %d was the answer?!" % x)
        break

if counter == 7:
    print("Better luck next time Champ!")
    print("Oh, by the way, the number was %d" % random_number)
