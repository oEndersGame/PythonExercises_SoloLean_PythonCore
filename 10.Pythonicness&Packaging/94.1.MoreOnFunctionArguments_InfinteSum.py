# Problem:
'''
Given a function that takes 2 arguments and returns their sum.
But we get an error when we want to sum more than 2 numbers. Change the function and complete the code so that the function sums as many numbers as are input.

NOTE: *args are accessible as the tuple args in the body of the function, so you can iterate through its items.
'''
#---------------------------------------------#

# CODE:

def adder(*x):
    print( sum(x))

adder(2, 3)
adder(2, 3, 4)
adder(1, 2, 3, 4, 5)