# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
#
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then,the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

user_input = input("Enter your input: ")
# user_input = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
frequency = {}

for word in user_input.split(" "):
    frequency[word] = frequency.get(word,0) + 1

words = frequency.keys()
list_of_words = list(words)
list_of_words.sort()#changes original order of list

for item in list_of_words:
    print(item + ':' + str(frequency[item]))
