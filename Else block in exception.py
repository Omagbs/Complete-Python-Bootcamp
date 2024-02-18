"""
This code illustrates the use of Try, except, and else blocks in python.
They are used for error exceptions
"""

try:
    print("I'm Batman")
    # if the the try blocks runs without error, then it skips the except block and moves to the else block
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")