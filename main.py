# ======================
# DATA MODEL
# ======================

inventory = [
    {"item_id": 1, "name": "Espresso", "unit_price": 2.50, "stock": 40},
    {"item_id": 2, "name": "Latte", "unit_price": 4.25, "stock": 25},
    {"item_id": 3, "name": "Cold Brew", "unit_price": 3.75, "stock": 30},
    {"item_id": 4, "name": "Mocha", "unit_price": 4.50, "stock": 20},
    {"item_id": 5, "name": "Blueberry Muffin", "unit_price": 2.95, "stock": 18},
]

orders = [
    {"order_id": "Order_101", "item_id": 2, "quantity": 2, "status": "Placed", "total": 8.50},
    {"order_id": "Order_102", "item_id": 3, "quantity": 1, "status": "Placed", "total": 3.75},
]

# ======================
# CREATE
# ======================

# Query 1: Place a new order for an item and quantity

# 1. Input:
item_id = int(input("Enter item ID: "))
quantity = int(input("Enter quantity: "))

# 2. Process:
selected_item = None
for item in inventory:
    if item["item_id"] == item_id:
        selected_item = item
        break

if selected_item is None:
    print("Item not found.")
elif quantity <= 0:
    print("Quantity must be at least 1.")
elif quantity > selected_item["stock"]:
    print("Not enough stock available.")
else:
    selected_item["stock"] -= quantity
    total = quantity * selected_item["unit_price"]

    # Create the next order ID (Order_103, Order_104, ...)
    new_order_id = f"Order_{101 + len(orders)}"

    new_order = {
        "order_id": new_order_id,
        "item_id": item_id,
        "quantity": quantity,
        "status": "Placed",
        "total": total
    }

    orders.append(new_order)

    # 3. Output:
    print("Order placed.")
    print(new_order)


# ======================
# READ
# ======================

# Query 2: View all orders placed for a particular item — prompt the user to enter the item name

# 1. Input:
search_item = input("Enter item name: ").strip()

# 2. Process:
selected_item_id = None
for item in inventory:
    if item["name"].lower() == search_item.lower():
        selected_item_id = item["item_id"]
        break

# 3. Output:
if selected_item_id is None:
    print("Item not found in inventory.")
else:
    found = False
    for order in orders:
        if order["item_id"] == selected_item_id:
            print("Order ID:", order["order_id"])
            print("Quantity:", order["quantity"])
            print("Total:", order["total"])
            print("Status:", order["status"])
            print()
            found = True

    if not found:
        print("No orders found for this item.")


# Query 3: Calculate total number of orders placed for "Cold Brew"

# 1. Input:
# None

# 2. Process:
cold_brew_id = None
for item in inventory:
    if item["name"] == "Cold Brew":
        cold_brew_id = item["item_id"]
        break

count = 0
for order in orders:
    if order["item_id"] == cold_brew_id:
        count += 1

# 3. Output:
print("Total Cold Brew orders:", count)


# ======================
# UPDATE
# ======================

# Query 4: Update item stock quantity by item ID

# 1. Input:
item_id = int(input("Enter item ID to update: "))
new_stock = int(input("Enter new stock quantity: "))

# 2. Process:
updated = False
for item in inventory:
    if item["item_id"] == item_id:
        item["stock"] = new_stock
        updated = True
        break

# 3. Output:
if updated:
    print("Stock updated successfully.")
else:
    print("Item not found.")


# ======================
# REMOVE / DELETE
# ======================

# Query 5: Cancel an order and restore stock

# 1. Input:
cancel_order_id = input("Enter Order ID to cancel: ").strip()

# 2. Process:
order_to_cancel = None
for order in orders:
    if order["order_id"] == cancel_order_id:
        order_to_cancel = order
        break

if order_to_cancel is None:
    print("Order not found.")
else:
    if order_to_cancel["status"] == "Cancelled":
        print("Order is already cancelled.")
    else:
        order_to_cancel["status"] = "Cancelled"

        item_id = order_to_cancel["item_id"]
        quantity = order_to_cancel["quantity"]

        for item in inventory:
            if item["item_id"] == item_id:
                item["stock"] += quantity
                break

        # 3. Output:
        print("Order cancelled successfully.")

    print(order_to_cancel)