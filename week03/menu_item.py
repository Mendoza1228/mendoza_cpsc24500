
print()
print("*" * 30)
print(f"{'STARLIGHT COFFEE POS':^30}")
print("*" * 30)

class MenuItem:
    # Initialize a menu item with its name, size, base price, and size upcharge
    def __init__(self, name, size, base_price, size_upcharge):
        self.name = name
        self.size = size
        self.price = base_price + size_upcharge

        

    def __str__(self):
        # Return a string representation of the menu item, including its name, size, and price
        return f"{self.name} ({self.size}) - ${self.price:.2f}"

