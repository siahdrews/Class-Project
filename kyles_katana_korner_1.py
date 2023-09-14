# Kyle's Katana Korner
# File: kyles_katana_korner_1.py
# Version: 1
# Description: POS program

#--------------CONSTANTS---------------#
KATANA_COST = 129.99 #cost of katana for customer

#TODO: Get int inpt for # of katanas
num_katanas = int(input("Enter number of katanas: "))

#TODO: Calculate price of katana(s) purchased
total_receipt = num_katanas * KATANA_COST

#TODO: Display transaction per customer
print(45*'-')
print(f"Katana's purchased:     {num_katanas}")
print(f"Price per katana        ${KATANA_COST}")
print(45*'-')
print(f'TOTAL:                  ${total_receipt}')