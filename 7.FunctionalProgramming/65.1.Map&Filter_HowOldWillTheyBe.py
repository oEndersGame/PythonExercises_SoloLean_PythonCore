# Problem:
'''
Given a list of birth years, calculate how old these people will be in the year 2050, and output the resulting list.
Recall, the map function allows you to apply a given function to all items of a list.

For example, a person born in 1995 will be 55 in the year 2050. So, to calculate the ages, you need to subtract the birth year from 2050.

NOTE: Remember, you need to explicitly convert the result of the map function to a list.
'''
#---------------------------------------------#

# CODE:

birth_years = [1995, 2004, 2019, 1988, 1977, 1902]

#your code goes here
m = list(map(lambda x: 2050 - x, birth_years))
print(m)