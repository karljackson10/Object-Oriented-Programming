#Exercise 4

from library import Library
from book import Book


library = Library()
book1 = Book('Three Musketeers', 'Alexandre Dumas', 'fiction')
book2 = Book('The Count of Monte Cristo', 'Alexandre Dumas', 'fiction')
book3 = Book('Educated', 'Tara Westover', 'nonfiction')

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.sort_books()

print(library.books)
print()
print(library.fiction)
print()
print(library.nonfiction)
print()
print(library.search_author('Alexandre Dumas'))
print()
print(library.search_author('Herman Melville'))
print()
print(library.search_title('Educated'))
print()
print(library.search_title('Moby Dick'))
