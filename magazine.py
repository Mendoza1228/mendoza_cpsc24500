from library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue, month, checked_out=False):
        super().__init__(title, author, year, checked_out)
        self._issue= issue
        self._month = month

    def get_item_type(self):
        return "Magazine"
    
    def __str__(self):
        return f"{super().__str__()} - Issue: {self._issue}, Month: {self._month}"
    
    @property
    def extra1(self):
        return self._issue
    
    @property
    def extra2(self):
        return self._month
    