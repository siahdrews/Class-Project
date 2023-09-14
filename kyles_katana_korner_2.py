# Kyle's Katana Korner
# File: kyles_katana_korner_2.py
# Version: 2
# Description: POS program with functions

#--------------CONSTANTS---------------#
KATANA_COST = 129.99 #cost of katana for customer


#---------------MAIN FUNCTION---------------#
def main():
    #---------------CALL FUNCTIONS---------------#
    num_katanas = get_input()
    total_sale = calculate(num_katanas)
    display(total_sale, num_katanas)

def get_input():
    #TODO: Get int inpt for # of katanas
    number_of_katanas = int(input("Enter number of katanas: "))
    return number_of_katanas #return user input for # of katanas

def calculate(num_katanas):
    #TODO: Calculate price of katana(s) purchased
    total = num_katanas * KATANA_COST
    return total #return calculated total cost of purchase

def display(total_sale, num_katanas):
    #TODO: Display transaction per customer
    print(35*'-')
    print(f"|Katana's purchased:     {num_katanas}")
    print(f"|Price per katana        ${KATANA_COST:,.2f}")
    print(35*'-')
    print(f'|TOTAL:                  ${total_sale:,.2f}')


if __name__ == '__main__':
    main()