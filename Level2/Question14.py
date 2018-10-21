#!/bin/python3

# Write a program that accepts a sentence and calculate the number of upper case
# letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

user_input = input("Enter sentence to calculate letter and or number count: ")

counted_items = {"UPPERCASE" :0,"LOWERCASE":0}

for item in user_input:
    if item.isupper():
        counted_items["UPPERCASE"] +=1
    elif item.islower():
        counted_items["LOWERCASE"] += 1

print("UPPER CASE ",counted_items["UPPERCASE"])
print("LOWER CASE ",counted_items["LOWERCASE"])
