# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
#
# Your program should accept a sequence of comma separated passwords and will check
# them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.
#
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

import re

user_input = input("Enter your password: ")

list_of_input = user_input.split(",")
list_of_output = []

for item in list_of_input:
    if len(item) <6 or len(item) >12:
        continue #get out and take next item in list_of_input
    else:
        pass
    if not re.search("[a-z]",item):
        continue
    if not re.search("[A-Z]",item):
        continue
    if not re.search("[0-9]",item):
        continue
    if not re.search("[$#@]",item):
        continue

    list_of_output.append(item)

# print(list_of_output)
print(",".join(list_of_output))
