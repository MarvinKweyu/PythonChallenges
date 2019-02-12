#!/bin/python3

# Define a function which can print a dictionary where the keys are numbers
# between 1 and 20 (both included) and the values are square of keys.

def make_dictionary():

    the_dictionary = {}
    for number in range(1,21):
        the_dictionary[number] = number*2
    print(the_dictionary)
    return

make_dictionary()
