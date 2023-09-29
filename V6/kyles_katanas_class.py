# Kyle's Katana Korner
# File: kyles_katanas_class.py
# Version: 6
# Description: class for Kyle's Katana Korner program


#--------------CONSTANTS---------------#
KATANA_COST = 129.99 #cost of katana for customer

class KatanaKorner:
    def __init__(self):
        self.items = ['Katana', 'Longsword', 'Rapier', 'Cutlass']
        self.prices = [129.99, 149.99, 99.99, 79.99]
        # create empty cart
        self.cart = [0, 0, 0, 0]

    #--------- Class Properties -----------------#
    def get_items(self) -> list:
        return self.items

    def get_prices(self) -> list:
        return self.prices


    #------------ ADD ITEMS TO CART --------------#
    def add_to_cart(self, choice: int, quantity: int) -> str:
        """add items and quantity to cart
            choice: index # of list item
            quantity: number of items
            returns string representation of cart
        """
        try:
            index = int(choice) - 1
            if 0 <= index < len(self.items):
                item = self.items[index]
                self.cart[index] = quantity + self.cart[index]
                cart_item = f"{quantity} {item}(s) added to cart."
                return cart_item
            else:
                print("Invalid choice. Please select a valid item number.")
        except ValueError:
            print("Invalid input. Please enter a valid item number.")

    #------------------- DISPLAY CATALOGUE --------------#
    def display_catalogue(self) -> str:
        """Return catalogue items and pries as string"""
        display = ""
        for n in range(len(self.items)):
            # Increment for numbering of catalogue
            i = n + 1
            # Concatenate catalogue items for line by line display
            display += f"({i}) {self.items[n]}\t\t{self.prices[n]:.2f}\n"
        return display
    
    #--------------- DISPLAY ORDER -----------#
    def display_order(self) -> str:
        """Display catalogue items and prices"""
        display = ""
        for n in range(len(self.items)):
            i = n + 1
            display += f"({i}) {self.items[n]}\t\t{self.prices[n]:.2f}\n"
        return display
    
    # ------------- CALCULATE TOTAL -------------#
    def calculate_total(self):
        """
            Calculate cost of items purchased
            Returns total cost of items
        """

        self.total = 0
        for i in range(3):
            self.total += self.cart[i] * self.prices[i]


    