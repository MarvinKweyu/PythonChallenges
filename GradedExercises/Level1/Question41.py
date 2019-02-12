#!/bin/python3

# Write a program to generate and print another tuple whose values are even
# numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

my_tuple = (1,2,3,4,5,6,7,8,9,10)
even_numbers = []

for number in my_tuple:
    if number%2 == 0:
        even_numbers.append(number)
print(tuple(even_numbers))
