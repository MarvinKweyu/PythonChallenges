#!/bin/python3

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

my_list =  [10, 15, 3, 7]
# k = int(input("Enter a number to check: "))
# k = 17

n = 181
n2 = n//2
numbers = [80, 98, 83, 92, 1, 38, 37, 54, 58, 89]
goodnums = {n-x for x in numbers if x<=n2} & {x for x in numbers if x>n2}
pairs = {(n-x, x) for x in goodnums}
print(pairs)

if not n%2 and (n2, n2) in pairs and numbers.count(n2) == 1:
   pairs.remove((n2, n2))

print(pairs)
