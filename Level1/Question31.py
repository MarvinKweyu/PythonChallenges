#!/bin/python3

# Define a function that can accept two strings as input and print the string
# with maximum length in console. If two strings have the same length,
# then the function should print all strings line by line.

def longest(word1,word2):

    if len(word1)> len(word2):
        print(word1)
    elif len(word2)>len(word1):
        print(word2)
    else:
        print(word1)
        print(word2)
    return

longest("one","twenty")
