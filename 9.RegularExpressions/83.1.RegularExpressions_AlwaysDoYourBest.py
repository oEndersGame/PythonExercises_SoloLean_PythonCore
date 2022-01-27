# Problem:
'''
Given the quote: "Always do your best. Your best is going to change from moment to moment; it will be different when you are healthy as opposed to sick. Under any circumstance, simply do your best, and you will avoid self-judgment, self-abuse and regret."
Complete the program so that it will take a word as input and output the number of times that word appears in the quote.

Sample Input:
best
Sample Output:
3

NOTE: Use re.findall to return a list of all substrings that match a pattern.
'''
#---------------------------------------------#

# CODE:

import re

quote = "Always do your best. Your best is going to change from moment to moment; it will be different when you are healthy as opposed to sick. Under any circumstance, simply do your best, and you will avoid self-judgment, self-abuse and regret"

word = input()
#your code goes here
print(len(re.findall(word,quote)))