class Catalog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Catalog, cls).__new__(cls)
            cls._instance._items = []
        return cls._instance
    
    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, title):
        self._items = [i for i in self._items if i.title.lower() != title.lower()]

    def search_by_title(self, keyword):
        return [i for i in self._items if keyword.lower() in i.title.lower()]
    
    def search_by_author(self, keyword):
        return [i for i in self._items if keyword.lower() in i.author.lower()]
    
    def get_all_items(self):
        return sorted(self._items)
    
    def get_checked_out_items(self):
        return [i for i in self._items if i.checked_out]
    
    def get_available_items(self):
        return [i for i in self._items if not i.checked_out]
    

    


    