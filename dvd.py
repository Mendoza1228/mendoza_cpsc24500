from library_item import LibraryItem

class DVD(LibraryItem):
    def __init__(self, title, author, year, runtime, rating, checked_out=False):
        super().__init__(title, author, year, checked_out)
        self._runtime = runtime
        self._rating = rating

    def get_item_type(self):
        return "DVD"

    def __str__(self):
        return f"{super().__str__()} | Runtime: {self._runtime} min, Rating: {self._rating}"

    @property
    def extra1(self): return self._runtime
    @property
    def extra2(self): return self._rating