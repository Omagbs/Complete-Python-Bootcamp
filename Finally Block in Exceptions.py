"""
This code illustrates the use of Try, except, else, and finaly blocks in python.
They are used for error exceptions
"""

try:
    print(x)
except:
    print("Something went wrong: error 404!")
    # the finally block still prints regardless. It's kinda like a default that happens anyway
finally:
    print("Try connecting to the internet")
