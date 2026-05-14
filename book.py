from library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, author, year, isbn, page_count, checked_out=False):
        super().__init__(title, author, year, checked_out)
        self._isbn = isbn
        self._page_count = page_count

    def get_item_type(self):
        return "Book"

    def __str__(self):
        return f"{super().__str__()} | ISBN: {self._isbn}, Pages: {self._page_count}"

    @property
    def extra1(self): return self._isbn
    @property
    def extra2(self): return self._page_count
    
    