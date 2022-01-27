# Problem:
'''
You are given coordinates of 2 points and need to find the straight line distance between them.
The coordinates are provided in a tuple, for example:
p = (8, 11)
The first value represents the x coordinate, while the second value represents the y coordinate of the point p.
Complete the provided code to calculate and output the distance between the two given points.

NOTE: The linear distance is the square root of the square of the horizontal distance plus the square of the
vertical distance between two points.
The math.sqrt() function can be used to calculate the square root.
'''
#---------------------------------------------#

# CODE:

import math

p1 = (23, -88)
p2 = (6, 42)

#your code goes here
result = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

print (result)
