#!/bin/python3

# Define a class, which have a class parameter and have a same instance parameter.
# Hints:
#     Define a instance parameter, need add it in __init__ method
#     You can init a object with construct parameter or set the value later

class Marvin(object):
    """docstring for Marvin."""
    def __init__(self, arg):
        super(Marvin, self).__init__()
        self.arg = arg
