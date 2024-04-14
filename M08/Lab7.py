#***************************************************************
# Author: Kyle Noyes
# Lab: 06
# Date: 2/17/2024
# Description: This program will calculate the total value of
#   coins given
# IDE console
# Input: INT penny, INT nickel, INT dime, INT quarter
# Output: total value of coins; data input error
# Sources: 
#***************************************************************
#START
#
#Hello! This program will calculate your coins total value 
#
#How many pennies do you have?: 5
#How many nickels do you have?: 1
#How many dimes do you have?: 9
#How many quarters do you have?: 4
#
#You have 19 coins
#
#The total value of your coins is: $2.00
#
#Would you like to re-run this program?
#Please enter 'y' or 'n': y
#How many pennies do you have?: 0
#How many nickels do you have?: 2
#How many dimes do you have?: 1
#How many quarters do you have?: 3
#
#You have 6 coins
#
#The total value of your coins is: $0.95
#
#Would you like to re-run this program?
#Please enter 'y' or 'n': n
#
#END
#***************************************************************

def main():
    keepGoing = 0

    # Welcome message
    msg_welcome()

    while (keepGoing == 0):
        #var declaration - also reset vars when re-run
        coins = []
        coinCount = 0
        totalValue = 0
        dataInvalid = []
        errorMsg = "\n"
    
        # Inputs
        coins = user_input(coins)

        # Validate program inputs are valid
        dataInvalid = data_validate(coins, dataInvalid)

        # If data valid, continue; if invalid, terminate program
        if len(dataInvalid) == 0:
            # Value calculation from Inputs
            totalValue = data_calc(coins)

            if data_valid(totalValue, "float") == 0:
                coinCount = count_coins(coins)
                msg_end(coinCount, totalValue)
            else:
                # This should never be reached, but will stop bad data going out
                errorMsg = "Internal program calculation error."
                msg_end_error(errorMsg)

        else:
            # Terminate program, alert user to which variable(s) broke
            errorMsg = error_decode(dataInvalid, errorMsg)
            msg_end_error(errorMsg)
        
        keepGoing = msg_continue()


def msg_welcome():
    """"
    Displays a simple welcome message. Can be easily edited
    """
    print("Hello! This program will calculate your coins total value \n")


def msg_end(coinCount, totalValue):
    """"
    Displays the final total
    :param coinCount: Int, contains calculated coin total
    :param totalValue: Float, coin values formated to 2 decimals
    """
    print("\nYou have {} coins\n".format(coinCount))
    print("The total value of your coins is: ${:.2f}".format(totalValue))


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


def input_valid(dataCheck, typeCheck):
    boolCheck = 0

    if typeCheck == "int":
        try:
            if (dataCheck % 1) == 0:
                boolCheck = 0
            else:
                boolCheck = 1
        except:
            boolCheck = 2

    if typeCheck == "float":
        try:
            # Checks if we have a decimal. Complex, but it's a good istype() substitute
            if (dataCheck % 1) > 0 and (dataCheck % 1) < 1 or str(dataCheck % 1) == 0.0:
                boolCheck = 0
            else:
                boolCheck = 1
        except:
            boolCheck = 2

    return boolCheck


def error_decode(dataInvalid, errorMsg):
    """"
    Decodes the error values to get specific problem value
    :param dataInvalid: list, contains all error conditions and related var
    :param errorMsg: string, constructing string to send to user later
    :return: string, errorMsg
    """
    for i in range(len(dataInvalid)):
        if dataInvalid[i] != "":
            errorMsg += msg_error_construct(dataInvalid[i])
    
    return errorMsg


def msg_continue(keepGoing=0):
    """"
    Repeast message and handler for related data
    :param keepGoing: int, boolean stand-in for returned true/false
    :return: Int keepGoing as 0 or 1
    """
    print("\nWould you like to re-run this program?")
    if get_y_or_n() == "y":
        keepGoing = 0
    else:
        keepGoing = 1

    return keepGoing


def user_input(coins):
    """"
    Gets user num of coins and stores values as integers
    :param coins: List, begins empty and then is appended to
    :return: List, coins
    """
    coins.append(get_integer("How many pennies do you have?: "))
    coins.append(get_integer("How many nickels do you have?: "))
    coins.append(get_integer("How many dimes do you have?: "))
    coins.append(get_integer("How many quarters do you have?: "))

    return coins


def data_validate(coins, dataInvalid):
    """"
    Validates if we have any bad data, check if less than zero
    :param coins: list, contains inputed values from user
    :param dataInvalid: list, appendeds offending var name if value < 0
    :return: list, dataInvalid
    """
    if coins[0] < 0:
        dataInvalid.append("Penny")
    
    if coins[1] < 0:
        dataInvalid.append("Nickel")
    
    if coins[2] < 0:
        dataInvalid.append("Dime")
    
    if coins[3] < 0:
        dataInvalid.append("Quarter")

    return dataInvalid


def data_calc(coins):
    """"
    Calculates the total value of coins in a typical USD format 1.00
    :param coins: List, contains user inputed quantities of coins
    :param totalValue: Int from penny*5 + nickel*5 dime*10 quarter*25
    :param totalValue: totalValue / 100
    :return: Float totalValue
    """
    totalValue = (coins[0] * 1) + (coins[1] * 5) + (coins[2] * 10) + (coins[3] * 25)
    totalValue = float(totalValue / 100)

    return totalValue


def count_coins(coins):
    """"
    Adds together total number of coins, it's a fun For loop
    :param coins: List, contains user inputed quantities of coins
    :param coinCount: Int, added total of all nums in list coins
    :return: Int, coinCount
    """
    coinCount = 0
    for i in range(len(coins)):
        coinCount += coins[i]
    
    return coinCount


def data_valid(dataCheck, typeCheck, boolCheck=0):
    """"
    Internal data validation tool
    :param dataCheck: Function Parameter, data to be checked
    :param typeCheck: Function Parameter, specify data comparison type
    :param boolCheck: Int, retainer for Bool check result
    :return: boolCheck as 0 / 1 / 2 as substitute to True / False / Invalid
    """

    if typeCheck == "int":
        try:
            if (dataCheck % 1) == 0:
                boolCheck = 0
            else:
                boolCheck = 1
        except:
            boolCheck = 2

    if typeCheck == "float":
        try:
            # Checks if we have a decimal. Complex, but it's a good istype() substitute
            # the str compare is not great... but it works and is easy to read
            if (dataCheck % 1) > 0 and (dataCheck % 1) < 1:
                boolCheck = 0
            elif (str(dataCheck % 1) == "0.0"):
                boolCheck = 0
            else:
                boolCheck = 1
        except:
            boolCheck = 2

    if typeCheck == "string":
        try:
            dataCheck + "Hello world :)"
            boolCheck = 0
        except:
            boolCheck = 2

    return boolCheck


# -- imported functions from lab 6 instructions -- #
def get_integer(prompt="Please enter an integer: "):
    """
    Function to prompt for and return a valid integer.
    :param prompt: string Optional string to use as prompt
    :return: integer Valid integer
    """
    num = 0
    while True:
        try:
            num = int(input(prompt))
            return num
        except:
            print("Invalid integer.")


def get_real(prompt="Please enter an real number: "):
    """
    Function to prompt for and return a valid real number
    :param prompt: string Optional string to use as prompt
    :return: float Valid real number
    """
    num = 0.0
    while True:
        try:
            num = float(input(prompt))
            return num
        except:
            print("Invalid number.")


def get_string(prompt="Please enter a string: "):
    """
    Function to prompt for and return a string of characters.
    An empty string is invalid input.
    :param prompt: string Optional string to use as prompt
    :return: string Non-empty string of characters
    """
    chars = ""
    while True:
        chars = input(prompt)
        if chars != "":
            return chars
        else:
            print("Invalid string.")


def get_y_or_n(prompt="Please enter 'y' or 'n': "):
    """
    Function to prompt for and return 'y' or 'n'.
    'Y', 'N', and all cases of 'yes' and 'no' are accepted.
    :param prompt: string Optional string to use as prompt
    :return: string Non-empty string of characters
    """
    answer = ""
    answer = input(prompt)
    answer = answer.lower()

    while answer != "n" and answer != "y" and answer != "no" and answer != "yes":
        print("Invalid response.")
        answer = input(prompt)
        answer = answer.lower()

    return answer
# ------------------------------------------------ #

main()