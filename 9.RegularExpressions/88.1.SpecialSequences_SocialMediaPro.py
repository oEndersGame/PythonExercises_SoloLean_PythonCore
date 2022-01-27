# Problem:
'''
You are a social media marketing specialist doing research on social networks.
Write a program for your research that will take text as input and output all of the hashtags in it separately.

Sample Input:
No #pressure, no #diamonds
Sample Output:
#pressure
#diamonds

NOTE: Remember that the re.findall() method returns a list of all substrings that match a pattern. So, you can use
the regex r"#\w+" to find all words that start with a hashtag and output them on separate lines.
'''
#---------------------------------------------#

# CODE:

import re
text = input()
#your code goes here
#use re.findall() with r"#\w+" as the regex
match = re.findall(r"#\w+", text)
if match:
    print("\n".join(match))