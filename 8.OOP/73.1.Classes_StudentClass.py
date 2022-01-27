# Problem:
'''
The provided code defines a Student class, creates a Student object, and calls its greet() method.
However, the code has an error and does not run.
Fix the code to produce the expected output.

NOTE: Hint: All methods need to have self as their first parameter.
'''
#---------------------------------------------#

# CODE:

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(self.name + " says hi")

obj = Student("John")
obj.greet()