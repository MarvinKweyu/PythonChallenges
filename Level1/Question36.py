#!/bin/python3

# Define a function which can generate and print a list where the values are
# square of numbers between 1 and 20 (both included).

def make_list():
    my_list = [value*2 for value in range(1,21)]
    print(my_list)
    return
make_list()
