# Problem:
'''
The university gives students discounts on tuition fees depending on their performance:
90-100 => 50%
80-89 => 30%
70-79 => 10%
0-69 => 0%
Write a program that will take the scores from the first and second semesters, then calculate the average score, and output the discount, depending on the score.

Sample Input:
67
83
Sample Output:
10

Explanation
Average of 67 and 83 is 75, which is in range of 70 to 79 and gets a 10% discount. Do not include the % symbol in the output.

NOTE: Average is the sum of numbers divided by quantity of that numbers. For example average of 5,6,7 is (5+6+7)/3 = 6.
'''
#---------------------------------------------#

# CODE:

score1 = int(input())
score2 = int(input())

avg = ((score1 + score2) / 2)

if avg >= 90 and avg <= 100:
    print (50)
elif avg >= 80 and avg <= 89:
    print (30)
elif avg >= 70 and avg <= 79:
    print (10)
else:
    print (0)