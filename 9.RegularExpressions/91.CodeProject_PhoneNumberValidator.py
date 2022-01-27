# Problem:
'''
You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
Output "Valid" if the number is valid and "Invalid", if it is not.

Sample Input:
81239870
Sample Output:
Valid

NOTE: You can use a regular expression to check if the input matches the given pattern.
'''
#---------------------------------------------#

# CODE:

import re
a = input()
pattern = r"[189]"
if re.match(pattern,a):
    if len(a) == 8:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")