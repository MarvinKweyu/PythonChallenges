#!/bin/python3
#
# Write a program which accepts a sequence of comma separated 4 digit binary numbers
# as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.

user_input = input("Enter your 4 digit numbers seperated by comma: ")

list_of_numbers = user_input.split(",")

divisible_by_five  = []

number = 0
for item in list_of_numbers:
    number = int(item)
    if number%5 == 0:  #alternatively (if not number%5:)
        divisible_by_five.append(str(number))

print(",".join(divisible_by_five))
