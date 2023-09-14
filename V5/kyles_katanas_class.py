# Kyle's Katana Korner
# File: kyles_katanas_class.py
# Version: 5
# Description: class for Kyle's Katana Korner program


#--------------CONSTANTS---------------#
KATANA_COST = 129.99 #cost of katana for customer

class KatanaKorner:
    def __init__(self):
        pass

    def get_number_katanas(self):
        # validation
        if self._number_of_katanas > 0:
            return self._number_of_katanas
        else:
            return "You must order at least 1 Katana"

    def get_total_sale(self):
        return self._total_sale

    def calculate(self, number_of_katanas):
        #TODO: Calculate price of katana(s) purchased
        self._number_of_katanas = number_of_katanas
        self._total_sale = number_of_katanas * KATANA_COST #total sale = number of katanas * cost per katana

    