"""
This code illustrates the use of raise exception. The raise exception is used when you want to customize your own error
They are used for error exceptions
"""

x = -1
if x < 0:
    raise Exception("Error 99: No number below 0 is allowed")

# or

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers allowed")
