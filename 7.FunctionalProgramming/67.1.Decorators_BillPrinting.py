# Problem:
'''
You are working on a restaurant software, which has a function to print the bill.

You need to add a decorator, which adds 3 hashtags before and after the bill data, so that the start and end of the printed bill can be identified.

Add a decorator to the code that adds ### before and after the print_bill() method.

NOTE: Do not forget to apply the decorator to the print_bill() method.
'''
#---------------------------------------------#

# CODE:

def decor(func):
    def wrap():
        #your code goes here
        print("###")
        func()
        print("###")
    return wrap

def print_bill():
    print("BILL DATA GOES HERE")

decorated = decor(print_bill)
decorated()