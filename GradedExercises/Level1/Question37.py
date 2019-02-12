#!/bin/python3

# Define a function which can generate a list where the values are square of
# numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

def make_list():
    my_list = [value for value in range(1,21)]
    print(my_list[-5:])
    return
make_list()
