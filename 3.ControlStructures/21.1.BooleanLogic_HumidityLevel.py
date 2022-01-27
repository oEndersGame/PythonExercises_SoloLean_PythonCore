# Problem:
'''
The comfortable relative humidity for humans is between 40% and 60%.
The given program takes the percent of humidity as input.

Task
Complete the code to output "norm" if the taken percent of humidity is in the range of 40 and 60 inclusive.
Don't output anything otherwise.

Sample Input:
45
Sample Output:
norm

NOTE: Use the and operator to chain the conditions in the if statement.
'''
#---------------------------------------------#

# CODE:

humidity = int(input())
if humidity >= 40 and humidity <= 60 :
  print ("norm")