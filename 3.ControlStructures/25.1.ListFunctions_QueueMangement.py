# Problem:
'''
You are working on a queue management program.
The queue is represented by a list.
Write a program to take an input, add it to the end of the queue and output the resulting list.

NOTE: The append() method can be used to add new items to the list.
'''
#---------------------------------------------#

# CODE:

queue = ["John", "James", "Amy"]

txt = input()
queue.append(txt)
print(queue)