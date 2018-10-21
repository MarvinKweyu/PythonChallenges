#!/bin/python3

# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

user_input = input("Enter values for the list seperated by comma: ")

list_of_input = user_input.split(",")
list_of_output = []

for num in range(0,(len(list_of_input)+1),2):
    list_of_output.append(num)
print(list_of_output)
