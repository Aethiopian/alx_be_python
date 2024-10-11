# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"You have checked out '{title}'.")
                    return
        print(f"Sorry, '{title}' is not available.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"You have returned '{title}'.")
                    return
        print(f"Sorry, '{title}' was not checked out.")

    def list_available_books(self):
        available_books = [book.title for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books available.")
