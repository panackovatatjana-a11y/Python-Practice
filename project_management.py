# Simple Book class
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

# Simple Library class
class Library:
    def __init__(self):
        self.books = []  # array (list)

    def add_book(self, book):
        self.books.append(book)

    def search_title(self, title):
        return list(filter(lambda b: b.title == title, self.books))

    def search_author(self, author):
        return list(filter(lambda b: b.author == author, self.books))

    def update_availability(self, title, status):
        for book in self.books:
            if book.title == title:
                (lambda b: setattr(b, "available", status))(book)

# --- Testing ---
library = Library()

# Add books
library.add_book(Book("Harry Potter", "J.K. Rowling"))
library.add_book(Book("1984", "George Orwell", False))

# Search
print(library.search_title("1984"))
print(library.search_author("J.K. Rowling"))

# Update
library.update_availability("1984", True)
print(library.search_title("1984"))
