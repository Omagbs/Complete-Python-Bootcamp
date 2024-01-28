# This code illustrate how to format strings in python

# An example:
name = "Wayne"
age = 8
print("Name = %s and Age = %d" % (name, age))

# This can also be formatted as
print("Name = %s and Age = %d" % ("Batman", 20))

# Note When formatting strings
# %s = strings
# %d or %i = signed integer
# %f = floating point
# %c = character
# %u = unsigned decimal integer
# %o = octal integer
# %x or %X = hexadecimal integer
# %e or %E = exponential notation
# %g or %G = short numbers in floating point oe exp notations

# An example:
i = 1
j = 2
print("i = %i \t j = %d \t" % (i, j))

# An example:
Ch = 'T'
i = 5
j = 6.7
str1 = "Hello"
print("Ch = %c, i = %i, j = %f, and str1 = %s" % (Ch, i, j, str1))

