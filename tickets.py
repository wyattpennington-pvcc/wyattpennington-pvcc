# Name: Wyatt Pennington
# Prog Purpose: this program finds the cost of movie tickets
#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%

import datetime

##############  define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET = 10.99

# define global variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

##############  define program functions ################
def main():

    more_tickets = True

    while more_tickets:
        get_user_data()
        preform_calculations()
        display_results()

        askAgain = input("\nWould you like to order again (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            more_tckets = False
            print("Thank you for order. enjoy your movie!")

def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

def preform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('-----------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your meighborhood movie house')
    print('-----------------------')
    print('Tickets   $ ' + str(subtotal))
    print('Sales tax   $ ' + str(sales_tax))
    print('Total   $ ' + str(total))
    print('-----------------------')
    print(str(datetime.datetime.now()))

##########  call on main program to execute ############
main()
