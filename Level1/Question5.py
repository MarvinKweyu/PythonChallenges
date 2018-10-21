#!/bin/python3

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#


class Marvin(object):

    def __init__(self):
        self.string = " " #no return value

    def get_string(self):
        self.string = input("Enter string: ")

    def print_string(self):
        'return string in uppercase'
        print(self.string.upper())

user = Marvin()
user.get_string()
user.print_string()
