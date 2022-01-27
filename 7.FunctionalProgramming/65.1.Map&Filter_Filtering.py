# Problem:
'''
Given a list of names, output a list that contains only the names that consist of more than 5 characters.

NOTE: You can check the length of a string using the len() function and use the filter() function to define the condition.
'''
#---------------------------------------------#

# CODE:

names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]

#your code goes here
a = list(filter(lambda x: len(x) > 5, names))
print (a)