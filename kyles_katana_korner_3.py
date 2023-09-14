# Kyle's Katana Korner
# File: kyles_katana_korner_3.py
# Version: 3
# Description: OOP POS program



#--------------CONSTANTS---------------#
KATANA_COST = 129.99 #cost of katana for customer


class KatanaKorner:
    def __init__(self):
        pass

    def get_input(self):
        #TODO: Get int inpt for # of katanas
        self.num_katanas = int(input("Enter number of katanas: "))

    def calculate(self):
        #TODO: Calculate price of katana(s) purchased
        self.total_sale = self.num_katanas * KATANA_COST #total sale = number of katanas * cost per katana

    def display(self):
        #TODO: Display transaction per customer
        print(35*'=')
        print(f"||Katana's purchased:     {self.num_katanas}")
        print(f"||Price per katana        ${KATANA_COST:,.2f}") #cost per katana printed as dollars
        print(35*'=')
        print(f'||TOTAL:                  ${self.total_sale:,.2f}') #total cost of purchase

katana_korner = KatanaKorner()
 
katana_korner.get_input()
katana_korner.calculate()
katana_korner.display()