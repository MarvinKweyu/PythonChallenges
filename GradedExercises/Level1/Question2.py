#!/bin/python3

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

from math import factorial

number = int(input("Enter a number to print the factorial: "))
print(factorial(number))