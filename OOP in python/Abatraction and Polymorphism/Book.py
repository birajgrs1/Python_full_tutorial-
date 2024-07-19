class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):
        total_pages = self.pages + other.pages
        return Book("All Books", total_pages)

    def __str__(self):
        return str(self.pages)

b1 = Book('Muna madan', 41)
b2 = Book('You can win', 314)
b3 = Book('Harry potter', 607)

total_pages = b1 + b2 + b3
print("Total no of pages:", total_pages)
