# Problem:
'''
Write a program that takes a word as input, and outputs "Match" if the word has 4 letters, starts with "m" and ends with "e".
The program should output "No match" if these mentioned requirements aren't satisfied.

Sample Input:
mine
Sample Output:
Match

NOTE: Don't forget to mention the start and end of the regular expression.
'''
#---------------------------------------------#

# CODE:

import re

word = input()
#your code goes here
if re.match('m..e', word):
    print("Match")
else:
    print("No match")