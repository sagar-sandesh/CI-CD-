import pytest
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if not self.available:
            return False
        self.available = False
        return True

    def return_book(self):
        self.available = True

    def test_book_borrow_success():
        book = Book("Clean Code", "Robert Cecil Martin")
        success = book.borrow()
        assert success is True
        assert book.available is False