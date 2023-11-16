# This code illustrates the generation of OTP using the Random module and maths module

import random, math  # Imports these modules

otp = ""  # initializes otp as a string

for i in range(1, 7):
    a = random.random() # calls random function from random module and store it in variable a
    b = math.floor(a * 10) # converts the number to single digit by multiplying it by 10. Floor function from math
    # module is called to round down to the nearest whole number
    otp += str(b) # stores the OTP digits for each iteration

print("Your one time password is: ", otp)
