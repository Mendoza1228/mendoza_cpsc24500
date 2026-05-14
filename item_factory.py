from book import Book
from dvd import DVD
from magazine import Magazine

class ItemFactory:
    @classmethod

    def create_item(cls, item_type, title, author, year, extra1, extra2, checked_out=False):
        t = item_type.strip().capitalize()
        if t == "Book":
            return Book(title, author,int(year), extra1, int(extra2), checked_out)
        elif t == "Dvd":
            return DVD(title, author,int(year), int(extra1), extra2, checked_out)
        elif t == "Magazine":
            return Magazine(title, author,int(year), int(extra1), extra2, checked_out)
        else:
            raise ValueError(f"Unknown item type: {item_type}")