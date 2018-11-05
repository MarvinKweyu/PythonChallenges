#!/bin/python3

# Define a function which can generate a dictionary where the keys are numbers
# between 1 and 20 (both included)
# and the values are square of keys. The function should just print the values only.

def make_dictionary():
    the_dictionary = {}
    for number in range(1,21):
        the_dictionary[number] = number*2
    for v in the_dictionary.values():
        print(v)
    return

make_dictionary()
