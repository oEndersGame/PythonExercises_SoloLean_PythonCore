# Problem:
'''
Given a string as input, create a generator function that splits the string into separate words and outputs the resulting list.

Sample Input:
This is some text
Sample Output:
['This', 'is', 'some', 'text']

NOTE: You can use the split() function to split the input string.
'''
#---------------------------------------------#

# CODE:

txt = input()

def words():
    #your code goes here
    for x in txt.split():
        yield x

print(list(words()))