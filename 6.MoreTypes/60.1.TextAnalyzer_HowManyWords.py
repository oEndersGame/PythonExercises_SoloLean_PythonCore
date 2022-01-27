# Problem:
'''
Given text as input, output the number of words it contains.

Sample Input:    hello world
Sample Output:   2

NOTE: The split() method can be used to split the string into words.
'''
#---------------------------------------------#

# CODE:

txt = input()

#your code goes here

words = txt.split()


#print(len(words))                # the easyier solution

# wort zähler                     # same solution using a function with a forLOOP
def count_words(words):
    count = 0
    for c in words:
        count += 1
    return count

print(count_words(words))