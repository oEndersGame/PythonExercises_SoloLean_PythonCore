# Problem:
'''
A coffee vending machine makes 5 types of coffee:
coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

Each coffee option has its own number, starting with 0. Write a program that will take a number from the customer as input from the customer and serve the corresponding coffee type. If the customer enters a number that is out of the accepted range, the program should output "Invalid number". Regardless of coffee option result, the program should output "Have a good day" at the end.

Sample Input:
7
Sample Output:
Invalid number
Have a good day

NOTE: Remember, that the first element of the list has 0 index.
'''
#---------------------------------------------#

# CODE:

coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

choice = int(input())

try:
    print(coffee[choice])        # your code goes here

except:
    if choice > len(coffee):
        print("Invalid number")  # and here

finally:
    print("Have a good day")     # and finally here