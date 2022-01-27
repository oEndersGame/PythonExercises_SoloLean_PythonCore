# Problem:
'''
Let's imagine we are creating our own authentication system.
Create a program that takes a password as input and returns "Password created" if
- it has at least one uppercase character
- it has at least one number

The Program should output "Wrong format" if requirements above are not met.

Sample Input:
Hal44gb8
Sample Output:
Password created

NOTE: Use metacharacter * that means zero or more repetitions.
'''
#---------------------------------------------#

# CODE:

import re
password = input()

#your code goes here
pattern = "[A-Z+].*[0-9+]"
if re.match(pattern,password):
    print("Password created")
else:
    print("Wrong format")