from menu_item import MenuItem
from order import Order





def main():
    print("Starlight Coffee POS System")
    customer_name = input("Enter your name: ")
    order = Order(customer_name)
    
    #Menu Data
    drink_menu = {
        "1": ("Americano", 3.50),
        "2": ("Cappuccino", 4.25),
        "3": ("Latte", 4.75),
        "4": ("Espresso", 3.00)
    }
       
    
    size_menu = {
        "1": ("Small", 0.00),
        "2": ("Medium", 0.75),
        "3": ("Large", 1.25)
    }

    

    while True:
        print("\n1. Add drink\n2. View Order\n3. Remove Drink\n4. Checkout")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n---Drinks---")
            for k, v in drink_menu.items():
                print(f"{k}. {v[0]} - ${v[1]:.2f}")
            drink_choice = input("Select a drink #: ")

            print("\n---Sizes---")
            for k, v in size_menu.items():
                print(f"{k}. {v[0]} (Upcharge: ${v[1]:.2f})")
            size_choice = input("Select a size #: ")

            if drink_choice in drink_menu and size_choice in size_menu:
                d_name, d_price = drink_menu[drink_choice]
                s_name, s_upcharge = size_menu[size_choice]
                new_item = MenuItem(d_name, s_name, d_price, s_upcharge)
                order.add_item(new_item)
            else:
                print("Invalid drink or size selection.")

        elif choice == "2":
            print(order)
        elif choice == "3":
            print(order)
            if order.items:
                rem_index = int(input("Enter the item number to remove: ")) - 1
                order.remove_item(rem_index)
        elif choice == "4":
            print(order)
            print("*" * 40)
            print(f"Thank you for your order, {order.customer_name}!")
            print("*" * 40)
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
