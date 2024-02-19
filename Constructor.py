"""
A constructor is activated upon object creation of a class

This code illustrates the use of a constructor in python
its syntax: __init__()
"""


class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello")
        print(self.name)


person = Person("Batman")
person.hello()

