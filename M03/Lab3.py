#***************************************************************
# Author: Kyle Noyes
# Lab: 03
# Date: 1/25/2024
# Description: This program will calculate the total value of
#   coins given
# IDE console
# Input: INT penny, INT nickel, INT dime, INT quarter
# Output: total value of coins added together
# Sources: 
#***************************************************************
#START

#Hello! This program will calculate your coins total value 

#How many pennies do you have?: 5
#How many nickels do you have?: 9
#How many dimes do you have?: 6
#How many quarters do you have?: 4

#The total value of your coins is: $2.10

#END
#***************************************************************

def main():
    #var declaration
    penny = 0
    nickel = 0
    dime = 0
    quarter = 0
    totalValue = 0

    # Welcome message
    msg_welcome()

    # Inputs
    penny, nickel, dime, quarter = user_input()

    # Value calculation from Inputs
    totalValue = data_calc(penny, nickel, dime, quarter)

    # Value dispaly & End message
    msg_end(totalValue)


def msg_welcome():
    """"
    Displays a simple welcome message. Can be easily edited
    """
    print("Hello! This program will calculate your coins total value \n")

def msg_end(totalValue):
    """"
    Displays the final total
    :param totalValue: Float, coin values formated to 2 decimals
    """
    print("\nThe total value of your coins is: ${:.2f}".format(totalValue))

def user_input():
    """"
    Gets user num of coins and stores balues as integers
    :param penny: int, number of pennies
    :param nickel: int, number of nickles
    :param dime: int, number of dimes
    :param quarter: int, number of quarters
    :return: Int Num penny, Int Num nickel, Int Num dime, Int Num quarter
    """
    penny = int(input("How many pennies do you have?: "))
    nickel = int(input("How many nickels do you have?: "))
    dime = int(input("How many dimes do you have?: "))
    quarter = int(input("How many quarters do you have?: "))
    return penny, nickel, dime, quarter

def data_calc(penny, nickel, dime, quarter):
    """"
    Calculates the total value of coins in a typical USD format 1.00
    :param totalValue: Int from penny*5 + nickel*5 dime*10 quarter*25
    :param totalValue: totalValue / 100
    :return: Float totalValue
    """
    totalValue = (penny * 1) + (nickel * 5) + (dime * 10) + (quarter * 25)
    totalValue = float(totalValue / 100)
    return totalValue

main()