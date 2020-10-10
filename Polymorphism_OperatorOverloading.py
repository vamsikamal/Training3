class Book:
    def __init__(self, p):
        self.pages = p

    def __add__(self, other):
        return self.pages + other.pages

    def __sub__(self, other):
        return self.pages - other.pages

    def __mul__(self, other):
        return self.pages * other.pages



book1 = Book(100)
book2 = Book(200)
print(book1 + book2)
print(book1 - book2)
print(book1 * book2)
