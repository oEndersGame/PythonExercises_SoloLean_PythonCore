# Problem:
'''
To order a restaurant dish online, the user should enter the code of desired dish, which contains only digits. Write a program that will take the code as input, and output "Enter only digits" if it contains non-digit symbols, and output "Order accepted" if it doesn't.
If the ordering process went well, the program also should output "Bon appetit".

Sample Input
1437

Sample Output
Order accepted
Bon appetit

NOTE: Use int() function to try to convert the input string to integer.
'''
#---------------------------------------------#

# CODE:

code = input()

#your code goes here
try:
    int(code)
except ValueError:
    print("Enter only digits")
else:
    print("Order accepted\n"+"Bon appetit")