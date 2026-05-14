class CatalogView:
    @staticmethod
    def display_menu():
        print("\n" + "="*29)
        print("Library Catalog System")
        print("="*29)
        print("1. List all items")
        print("2. Search by title")
        print("3. Search by author")
        print("4. Check out item")
        print("5. Check in item")
        print("6. Add new item")
        print("7. View checked-out items")
        print("8. Save and quit")

    @staticmethod
    def display_items(items, title="Items"):
        print(f"\n--- {title} ---")
        if not items:
            print("No items found.")
        for item in items:
            print(item)

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_search_results(items, query):
        CatalogView.display_items(items, f'Search Results for "{query}"')