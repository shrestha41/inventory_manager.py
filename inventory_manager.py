"""
Inventory Management Tool - Lesson 3 Individual Assignment
Processes a batch of customer orders against an in-memory inventory.
Uses only lists, dictionaries, tuples, loops, and conditionals.
"""

# ---------------- Task 1: Data setup ----------------
inventory = {"Widget": 10, "Gadget": 5, "Sensor": 0, "Cable": 15}

# Each order: [item name, requested quantity]
orders = [
    ["Widget", 3],    # full fulfillment
    ["Sensor", 2],    # out of stock
    ["Gadget", 7],    # partial fulfillment
    ["Cable", 15],    # full fulfillment (uses all stock)
    ["Gizmo", 4],     # invalid item
    ["Widget", 8],    # partial fulfillment (7 left)
    ["Cable", 1],     # out of stock after earlier order
]

unfulfilled = []      # [item, quantity that could not be supplied]
fully_fulfilled = 0   # count of completely fulfilled orders

# ---------------- Task 2: Process orders ----------------
print("=== Processing Orders ===")
for item, qty in orders:
    stock = inventory.get(item)   # None when the key does not exist

    if stock is None:
        print(f"ALERT: '{item}' does not exist in inventory. Order of {qty} rejected.")
        unfulfilled.append([item, qty])
    elif stock >= qty:
        inventory[item] = stock - qty
        fully_fulfilled += 1
        print(f"SUCCESS: {qty} x {item} fulfilled. Remaining stock: {inventory[item]}")
    elif stock > 0:
        remainder = qty - stock
        inventory[item] = 0
        unfulfilled.append([item, remainder])
        print(f"PARTIAL: {stock} x {item} shipped. {remainder} unfulfilled.")
    else:
        print(f"ALERT: {item} is out of stock. Order of {qty} cannot be filled.")
        unfulfilled.append([item, qty])

# ---------------- Task 3: Summary report ----------------
print("\n=== End-of-Batch Summary ===")
print("Final inventory:", inventory)
print("Fully fulfilled orders:", fully_fulfilled)
print("Unfulfilled items:")
if len(unfulfilled) == 0:
    print("  None - all orders fully supplied.")
else:
    for item, qty in unfulfilled:
        print(f"  - {item}: {qty} short")
