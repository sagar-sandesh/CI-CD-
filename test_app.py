from Library.library import Library

def test_borrow_book_available():
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    result = lib.borrow_book("Dune")
    assert result is True
    assert lib.books[0].available is False
