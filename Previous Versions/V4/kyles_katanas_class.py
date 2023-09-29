# Kyle's Katana Korner
# File: kyles_katanas_class.py
# Version: 4
# Description: class for Kyle's Katana Korner program


#--------------CONSTANTS---------------#
KATANA_COST = 129.99 #cost of katana for customer

class KatanaKorner:
    def __init__(self):
        pass

    def calculate(self, number_of_katanas):
        #TODO: Calculate price of katana(s) purchased
        self.number_of_katanas = number_of_katanas
        self.total_sale = number_of_katanas * KATANA_COST #total sale = number of katanas * cost per katana

    