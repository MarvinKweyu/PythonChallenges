#!/bin/python3

# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

import re

user_input = input("Enter sentence to calculate letter and or number count: ")

counted_items = {'LETTERS':0,'DIGITS':0}

for item in user_input:
    if item.isdigit():
        counted_items['DIGITS'] += 1
    elif item.isalpha():
        counted_items['LETTERS'] +=1

# print(counted_items)

print("LETTERS: ",counted_items['LETTERS'])
print("DIGITS: ",counted_items['DIGITS'])
