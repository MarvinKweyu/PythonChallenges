#!/bin/python3

# Define a function which can generate a dictionary where the keys are numbers
# between 1 and 20 (both included) and the values are square of keys.
# The function should just print the keys only.

def make_dictionary():
    the_dictionary = {}
    for number in range(1,21):
        the_dictionary[number] = number*2
    for k in the_dictionary.keys():
        print(k)
    return

make_dictionary()
