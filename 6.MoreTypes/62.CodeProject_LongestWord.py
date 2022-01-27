# Problem:
'''
Given a text as input, find and output the longest word.

Sample Input:
this is an awesome text
Sample Output:
awesome

NOTE: Recall the split(' ') method, which returns a list of words of the string.
'''
#---------------------------------------------#

# CODE:

txt = input().split()

print(max(txt, key = len))