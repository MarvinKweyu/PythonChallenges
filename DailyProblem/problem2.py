#!/bin/python3
import numpy as np

# Given an array of integers, return a new array such that each element at index i
# of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# user_input = input("Enter your list to make an array:(seperate by comma and press enter) ")
# my_list = user_input.split(',')
# print(my_list)

# my_list = [3, 2, 1]
my_list = [1, 2, 3, 4, 5]

final_list = []

for item in my_list:
    intermediate_list = []
    intermediate_list.extend(my_list)
    intermediate_list.remove(item)
    array1 = np.array(intermediate_list)
    product = array1.prod()
    final_list.append(product)

print(final_list)
