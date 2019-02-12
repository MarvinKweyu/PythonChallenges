#!/bin/python3

# Define a function which can generate and print a tuple where the value are
# square of numbers between 1 and 20 (both included).

def make_tuple():
    my_list = []
    for number in range(1,21):
        my_list.append(number*2)
    print(tuple(my_list))
    return

make_tuple()
