# Problem:
'''
You are given the following list:
names = ["John", "Oscar", "Jacob"]
Complete the program to create a file where you write the names from the list, each on a new line,
and separately output them.

Output:
John
Oscar
Jacob

NOTE: Remember that "\n" represents a new line.
'''
#---------------------------------------------#

# CODE:

names = ["John", "Oscar", "Jacob"]

file = open("names.txt", "w+")
#write down the names into the file
for i in names:
     file.write( i + "\n" )
file.close( )

file= open("names.txt", "r")
#output the content of file in console
print(file.read())
file.close()