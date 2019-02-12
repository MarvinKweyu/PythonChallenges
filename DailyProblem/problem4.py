# Given an array of integers, find the first missing positive integer in linear time
# and constant space. In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.
import numpy as np
from math import floor
# my_list = [3, 4, -1, 1]
my_list=[1, 2, 0]

array1 = np.array(my_list)


for number in my_list:
    field = [x for x in range(number+1)] #list of values leading to positive integer number
    if (number>0) and (field not in my_list):
        print(number)
    # elif (number>0) and field in my_list:
    #     print("Silly mistake")
