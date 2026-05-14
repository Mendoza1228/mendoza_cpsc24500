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
                item_type, title, author, year, ex1, ex2, status = parts
                is_out = status.lower() == 'true'
                item = ItemFactory.create_item(item_type, title, author, year, ex1, ex2, is_out)
                catalog.add_item(item)
                count += 1
    return count

def save_data(filename, catalog):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        for i in catalog.get_all_items():
            status = str(i.checked_out).lower()
            
            f.write(f"{i.get_item_type()}\t{i.title}\t{i.author}\t{i.year}\t{i.extra1}\t{i.extra2}\t{status}\n")

def main():
    catalog = Catalog()
    view = CatalogView()
    file_path = "data/catalog.tsv"
    
    loaded = load_data(file_path, catalog)
    view.display_message(f"Catalog loaded: {loaded} items.")

    while True:
        view.display_menu()
        choice = input ("Enter choice: ")

        try:
            if choice == '1':
                view.display_items(catalog.get_all_items(), "All Items (sorted by title)")
            elif choice == '2':
                q = input("Enter title to search: ")
                view.display_search_results(catalog.search_by_title(q), q)
            elif choice == '3':
                q = input("Enter author to search: ")
                view.display_search_results(catalog.search_by_author(q), q)
            elif choice == '4':
                title = input("Enter the exact title to check out: ")
                items = catalog.search_by_title(title)
                match = next((i for i in items if i.title.lower() == title.lower()), None)
                if match:
                    match.check_out()
                    view.display_message(f"Successfully checked out: {match.title}")
                else: view.display_message("Item not found.")
            elif choice == '5':
                title = input("Enter the exact title to check in: ")
                items = catalog.search_by_title(title)
                match = next((i for i in items if i.title.lower() == title.lower()), None)
                if match:
                    match.check_in()
                    view.display_message(f"Successfully checked in: {match.title}")
                else: view.display_message("Item not found.")
            elif choice == '6':
                itype = input("Item type (Book/DVD/Magazine): ")
                title = input("Title: ")
                author = input("Author: ")
                year = input("Year: ")
                ex1 = input("Extra field 1 (ISBN/Runtime/Issue): ")
                ex2 = input("Extra field 2 (Pages/Rating/Month): ")
                new_item = ItemFactory.create_item(itype, title, author, year, ex1, ex2)
                catalog.add_item(new_item)
                view.display_message(f"Added: {title}")
            elif choice == '7':
                view.display_items(catalog.get_checked_out_items(), "Checked-Out Items")
            elif choice == '8':
                save_data(file_path, catalog)
                view.display_message("Catalog saved. Goodbye!")
                break
            else:
                view.display_message("Invalid choice. Try again.")
        except (ValueError, RuntimeError) as e:
            view.display_message(f"Error: {e}")
        except Exception as e:
            view.display_message(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()


                
            