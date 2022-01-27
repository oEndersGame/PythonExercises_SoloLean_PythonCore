# Problem:
'''
A library management program has a dictionary of books with their corresponding genres.

Take a book name as input and output the genre.

NOTE: If the book is not present in the dictionary, output "Not found".
'''
#---------------------------------------------#

# CODE:

books = {
    "Life of Pi": "Adventure Fiction",
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics",
    "Bird Box": "Horror",
    "Harry Potter":"Fantasy Fiction",
    "Good Omens": "Comedy"
}

book = input()

try:
    print(books[book])
except KeyError:
    print('Not found')