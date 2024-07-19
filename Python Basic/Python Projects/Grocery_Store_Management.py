# Decorator for tracking item quantity after purchase or restock
def track_quantity(func):
    def wrapper(inventory, item_name, quantity, *args, **kwargs):
        result = func(inventory, item_name, quantity, *args, **kwargs)
        inventory[item_name]['quantity'] += quantity
        return result
    return wrapper

# Grocery management generator
def grocery_management():
    inventory = {}

    @track_quantity
    def add_item(inventory, item_name, quantity):
        if item_name not in inventory:
            inventory[item_name] = {'quantity': 0}
        print(f"Added {quantity} {item_name} to inventory")

    @track_quantity
    def purchase_item(inventory, item_name, quantity):
        if item_name in inventory and inventory[item_name]['quantity'] >= quantity:
            inventory[item_name]['quantity'] -= quantity
            print(f"Purchased {quantity} {item_name}")
        else:
            print(f"Insufficient stock for {item_name}")

    @track_quantity
    def restock_item(inventory, item_name, quantity):
        inventory[item_name]['quantity'] += quantity
        print(f"Restocked {quantity} {item_name}")

    @track_quantity
    def check_inventory(inventory, item_name, _):
        if item_name in inventory:
            return inventory[item_name]['quantity']
        else:
            return 0

    yield add_item
    yield purchase_item
    yield restock_item
    yield check_inventory

# Using the grocery management generator
manager = grocery_management()

while True:
    print("\nOptions:")
    print("1. Add Item")
    print("2. Purchase Item")
    print("3. Restock Item")
    print("4. Check Inventory")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_item = next(manager)
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        add_item(item_name, quantity)
    elif choice == '2':
        purchase_item = next(manager)
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        purchase_item(item_name, quantity)
    elif choice == '3':
        restock_item = next(manager)
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        restock_item(item_name, quantity)
    elif choice == '4':
        check_inventory = next(manager)
        item_name = input("Enter item name: ")
        quantity = check_inventory(item_name, 0)
        print(f"Inventory for {item_name}: {quantity}")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please select again.")
