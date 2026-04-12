
print()
print("*" * 40)
print(f"{'STARLIGHT COFFEE POS':^40}")
print("*" * 40)

class MenuItem:
    # Initialize a menu item with its name, size, base price, and size upcharge
    def __init__(self, name, size, base_price, size_upcharge):
        self.name = name
        self.size = size
        self.price = base_price + size_upcharge

        

    def __str__(self):
        # Return a string representation of the menu item, including its name, size, and price
        return f"{self.name} ({self.size}) - ${self.price:.2f}"

