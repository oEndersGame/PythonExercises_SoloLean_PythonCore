# Problem:
'''
Write a program that takes a number as input and
- returns its double, if the number is even
- returns its triple, if the number is odd
- returns 0, if number is 0

Sample Input:
1
Sample Output:
3
NOTE: An integer is even if it is divisible by two and odd if it is not even.
'''
#---------------------------------------------#

# CODE:

number = int(input())
if number == 0:
    print (0)
elif number % 2 ==0:
    print (number * 2)
else:
    print (number *3)