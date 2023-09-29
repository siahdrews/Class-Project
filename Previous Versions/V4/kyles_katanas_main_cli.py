# Kyle's Katana Korner
# File: kyles_katanas_class.py
# Version: 4
# Description: main cli for Kyle's Katana Korner program

import kyles_katanas_class as katana

def get_input():
        #TODO: Get int inpt for # of katanas
        num_katanas = int(input("Enter number of katanas: "))
        return num_katanas

def display():
        #TODO: Display transaction per customer
        number_of_katanas = katana_korner.number_of_katanas
        total_sale = katana_korner.total_sale
        print(35*'=')
        print(f"||Katana's purchased:     {number_of_katanas}")
        print(35*'=')
        print(f'||TOTAL:                  ${total_sale:,.2f}') #total cost of purchase

number_of_katanas = get_input()

# create katana korner object
katana_korner = katana.KatanaKorner()

katana_korner.calculate(number_of_katanas)
display()
