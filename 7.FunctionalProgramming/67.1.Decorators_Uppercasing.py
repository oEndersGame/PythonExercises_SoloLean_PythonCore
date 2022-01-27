# Problem:
'''
You are given code that takes input and prints it as a simple row of text.

Add the uppercase_decorator to make the text uppercase.

NOTE: The upper() method can be used on strings to make them uppercase.
'''
#---------------------------------------------#

# CODE:
text = input()

def uppercase_decorator(func):
    def wrapper(text):
        return text.upper()

    return wrapper

@uppercase_decorator
def display_text(text):
    return (text)

print(display_text(text))