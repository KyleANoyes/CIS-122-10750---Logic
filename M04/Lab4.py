#***************************************************************
# Author: Kyle Noyes
# Lab: 04
# Date: 2/02/2024
# Description: This program will calculate the total value of
#   coins given
# IDE console
# Input: INT penny, INT nickel, INT dime, INT quarter
# Output: total value of coins; data input error
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
    dataInvalid = 0 # Var number will update if errors are located
    errorMsg = "\n"

    # Welcome message
    msg_welcome()

    # Inputs
    penny, nickel, dime, quarter = user_input()

    # Validate program inputs are valid
    dataInvalid = data_validate(penny, nickel, dime, quarter, dataInvalid)

    # If data valid, continue; if invalid, terminate program
    if dataInvalid == 0:
        # Value calculation from Inputs
        totalValue = data_calc(penny, nickel, dime, quarter)

        # Value dispaly & End message
        msg_end(totalValue)
    else:
        # Terminate program, alert user to which variable(s) broke
        errorMsg = error_decode(dataInvalid, errorMsg)
        msg_end_error(errorMsg)
    


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

def msg_end_error(errorMsg):
    """"
    Displays the error message
    :param errorMsg: string, the final error to display
    """
    print(errorMsg)

def msg_error_construct(coinError):
    """"
    Displays a simple error message. Can be easily edited
    """
    return "Value {} is less than zero. Please restart this program.\n".format(coinError)

def error_decode(dataInvalid, errorMsg):
    """"
    Decodes the error values to get specific problem value
    :param penny: int, number of pennies
    :param nickel: int, number of nickles
    :param dime: int, number of dimes
    :param quarter: int, number of quarters
    :param errorMsg: string, constructing string to send to user later
    :return: string, errorMsg
    """
    if dataInvalid // 5000 == 1:
        dataInvalid = dataInvalid - 5000
        errorMsg = errorMsg + msg_error_construct("Quarter")

    if dataInvalid // 500 == 1:
        dataInvalid = dataInvalid - 500
        errorMsg = errorMsg + msg_error_construct("Dime")

    if dataInvalid // 50 == 1:
        dataInvalid = dataInvalid - 50
        errorMsg = errorMsg + msg_error_construct("Nickel")

    if dataInvalid // 5 == 1:
        dataInvalid = dataInvalid - 5
        errorMsg = errorMsg + msg_error_construct("Penny")
    
    return errorMsg

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

def data_validate(penny, nickel, dime, quarter, dataInvalid):
    # This is a silly solution, but it works. I would prefer to use 
    #   "x" in var, but this is the next viable method I can think of
    #   while keeping as single var. Also it was fun to code!
    """"
    Validates if we have any bad data, check if less than zero
    :param penny: int, number of pennies
    :param nickel: int, number of nickles
    :param dime: int, number of dimes
    :param quarter: int, number of quarters
    :param dataInvalid: int, 0 if no error, various 5's for errors
    :return: int, dataInvalid
    """
    if penny < 0:
        dataInvalid = dataInvalid + 5
    
    if nickel < 0:
        dataInvalid = dataInvalid + 50
    
    if dime < 0:
        dataInvalid = dataInvalid + 500
    
    if quarter < 0:
        dataInvalid = dataInvalid + 5000

    return dataInvalid

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