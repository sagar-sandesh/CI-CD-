from Book.books import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def is_available(self, title):
        for book in self.books:
            if book.title == title:
                return book.available
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.borrow()
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return True
        return False
