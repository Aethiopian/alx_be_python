# library_system.py

# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


# Derived class for EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # In MB

    def __str__(self):
        return f"{super().__str__()} [E-Book, File size: {self.file_size}MB]"


# Derived class for PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count  # Number of pages

    def __str__(self):
        return f"{super().__str__()} [Print Book, Pages: {self.page_count}]"


# Library class demonstrating composition
class Library:
    def __init__(self):
        self.books = []  # A collection of books

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)
