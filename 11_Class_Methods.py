class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example
b1 = Book("Python Basics")
b2 = Book("OOP Concepts")
print(Book.total_books)
