import os
from catalog import Catalog
from item_factory import ItemFactory
from catalog_view import CatalogView

def load_data(filename, catalog):
    if not os.path.exists(filename):
        return 0
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 7:
                item_type, title, author, year, extra1, extra2, checked_out = parts
                item = ItemFactory.create_item(item_type, title, author, year, extra1, extra2, checked_out)
                catalog.add_item(item)
                count += 1
    return count

def save_data(filename, catalog):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'W') as f:
        for i in catalog.get_all_items():
            status = str(i.is_checked_out).lower()
            f.write(f"{i.get_item_type()}\t{i.title}\t{i.author}\t{i.year}\t{i.extra1}\t{i.extra2}\t{status}\n")

                
            