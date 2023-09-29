# Kyle's Katana Korner
# File: kyles_katanas_class.py
# Version: 6
# Description: main cli for Kyle's Katana Korner program

import kyles_katanas_class as swords

# Main ordering loop
def start_order():
    while True:
        # print catalogue for each order
        print(kyle.display_catalogue())
        choice = input("Enter an item to order (q to quit): ").lower()

        if choice == 'q':
            break

        quantity = int(input("Enter the quantity: "))

        # Add items to cart and return cart string
        cart_item = kyle.add_to_cart(choice, quantity)
        print(cart_item)


# Genrate receipt
def generate_receipt():
    kyle.calculate_total()
    print("\nReceipt:")

    print(f"Total: ${kyle.total:.2f}")
    print("Thank you for your order!")


# Create KatanaKorner object
kyle = swords.KatanaKorner()
start_order()
generate_receipt()