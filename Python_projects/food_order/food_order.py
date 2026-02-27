menu = {
    "Burger": 4,
    "Hotdog": 3,
    "Pizza": 18,
    "Chicken": 8
}

print("--- Welcome to our Shop ---")
print("Menu:")
for item, price in menu.items():
    print(f"{item} - {price} euros")
print("-" * 25)

orders = []

while True:
    item = input("What food would you like? (type 'done' to finish): ").capitalize()

    if item.lower() == "done":
        break
    elif item not in menu:
        print("Invalid item. Please choose from the menu.")
        continue
    else:
        quantity = int(input(f"How many {item}s do you want? "))
        if quantity > 0:
            orders.append((item, quantity))

print("\n--- Your Order Summary ---")
for order in orders:
    print(f"{order[0]} x {order[1]}")

total = sum([menu[order[0]] * order[1] for order in orders])

print("-" * 25)
print(f"Your total is: {total} euros")
print("Thank you for your order!")
