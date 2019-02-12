#!/bin/python3

# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.
#
# Hints:
# Consider use yield

class MadeUp(object):

    values_divisible_by_seven = [] #class attribute

    def __init__(self,end):
        'initialize attributes'
        # self.start = start
        self.end = end

    def find_divisibles(self):
        'Iterate via range to find divisibles'
        for number in range(0,self.end):
            if number%7==0:
                self.values_divisible_by_seven.append(number)
        print(self.values_divisible_by_seven)

#main
user_input = int(input("Enter number in range to find divisibles of 7 between 0 and the number: "))
look_through = MadeUp(user_input)
look_through.find_divisibles()
