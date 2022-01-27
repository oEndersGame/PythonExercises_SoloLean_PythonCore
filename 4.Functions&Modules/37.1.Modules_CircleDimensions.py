# Problem:
'''
You are given a program that takes the radius of a circle as the input.
Complete the code to calculate the circle's perimeter and output the result.
Remember, the perimeter of a circle = 2*pi*radius

Sample Input:
5
Sample Output:
31.42

Hint
You need to import the pi constant from the math module to perform the calculation.

NOTE: The round() function in the code is used to round the decimal places of the output.
'''
#---------------------------------------------#

# CODE:

r = int(input())
from math import pi
def circle (x):
    print (round((2*pi*x),2))

circle(r)