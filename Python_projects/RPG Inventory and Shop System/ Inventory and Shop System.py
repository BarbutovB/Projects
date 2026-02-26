# Shop Data
shop_stock = {
    "Health Potion": 10,
    "Mana Potion": 5,
    "Sword": 1,
    "Shield": 2
}

prices = {
    "Health Potion": 50,
    "Mana Potion": 40,
    "Sword": 300,
    "Shield": 250
}

# Player Data
my_inventory = {}
my_gold = 500

def buy_item(item):
    global my_gold
    
    if item not in shop_stock or shop_stock[item] <= 0:
        print(f"--- Error: {item} is out of stock! ---")
        return

    if my_gold < prices[item]:
        print(f"--- Error: Not enough gold for {item}! ---")
        return

    # Process Transaction
    my_gold -= prices[item]
    shop_stock[item] -= 1
    
    if item not in my_inventory:
        my_inventory[item] = 0
    my_inventory[item] += 1
    
    print(f"Purchased {item}. Gold left: {my_gold}")

# Test Simulation
buy_item("Health Potion")
buy_item("Sword")
buy_item("Sword")

print("\n--- FINAL STATE ---")
print(f"My Gold: {my_gold}")
print(f"My Inventory: {my_inventory}")
print(f"Shop Stock: {shop_stock}")
