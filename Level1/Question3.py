#!/bin/python3

# With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def main():

    user_input = int(input("Enter a number to make a dictionary: "))

    list_of_keys = []
    list_of_values = []

    make_list_of_keys(list_of_keys,user_input)
    make_list_of_values(list_of_keys,list_of_values)
    dictionary = dict(zip(list_of_keys,list_of_values))
    print(dictionary)
    return

def make_list_of_keys(list_of_keys,user_input):
    for number in range(1,user_input+1):
        list_of_keys.append(number)
    return list_of_keys

def make_list_of_values(make_list_of_keys,list_of_values):

    for num in make_list_of_keys:
        prod = num * num
        list_of_values.append(prod)
    return list_of_values

main()
