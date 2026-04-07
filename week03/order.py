



class Order:
    # Initialize an order with the customer's name and an empty list of items
    def __init__(self, customer_name):
        self.items = []
        self.customer_name = customer_name
        self.tax_rate = 0.0875
    # Add an item to the order
    def add_item(self, menu_item):
        # Add the item to the order's list of items
        self.items.append(menu_item)
        print (f"Added: {menu_item}")
    # Remove an item from the order by its index (1-based)    
    def remove_item(self, index):
        # Remove the item from the order's list of items
        if 0 <= index < len(self.items):
            removed = self.items.pop(index -1)
            print(f"Removed: {removed}")
        else:
            print("Invalid item number.")
    # Calculate the subtotal of the order (sum of item prices)        
    def subtotal(self):
        return sum(item.price for item in self.items)
    # Calculate the tax for the order
    def tax(self):
        
        return self.subtotal() * self.tax_rate
    # Calculate the total price of the order, including tax
    def total(self):
        return self.subtotal() + self.tax()
        
    # Return a string representation of the order, including item details and total price
    def __str__(self):
        receipt = f"---Starlight Coffee POS ---\n"
        receipt = f"\n--- {self.customer_name}'s Receipt ---\n"
    
        for i, item in enumerate(self.items, 1):
            receipt += f"{i}. {item}\n"
        receipt += f"Subtotal: ${self.subtotal():.2f}\n"
        receipt += f"Tax (8.75%): ${self.tax():.2f}\n"
        receipt += f"Total: ${self.total():.2f}\n"
        receipt += f"Thank you for your order!"
        return receipt
    
    
    
