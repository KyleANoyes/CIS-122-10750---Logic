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
    keepGoing = 0

    # Welcome message
    msg_welcome()

    while (keepGoing == 0):
        # Inputs
        penny, nickel, dime, quarter = user_input()

        # Validate program inputs are valid
        dataInvalid = data_validate(penny, nickel, dime, quarter, dataInvalid)

        # If data valid, continue; if invalid, terminate program
        if dataInvalid == 0:
            # Value calculation from Inputs
            totalValue = data_calc(penny, nickel, dime, quarter)

            if data_valid(totalValue, "float") == 0:
                msg_end(totalValue)
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


# Legacy function for reference material
#def true_false(boolCheck=0, trueFalse=0):
#    """"
#    Acts as a boolean operator in place of True False declarations
#    :param booCheck: int, boolean stand-in for loop
#    :param trueFalse: int, boolean stand-in for returned true/false
#    :return: Int trueFalse as 0 or 1
#    """
#    while (boolCheck != 1):
#        trueFalse = int(input("Enter 0 to continue, or 1 to stop: "))
#        if trueFalse == 0:
#            boolCheck = 1
#        elif trueFalse == 1:
#            boolCheck = 1
#        else:
#            print("\nInvalid input. Input must be 0 or 1")
#
#    return trueFalse

def user_input():
    """"
    Gets user num of coins and stores balues as integers
    :param penny: int, number of pennies
    :param nickel: int, number of nickles
    :param dime: int, number of dimes
    :param quarter: int, number of quarters
    :return: Int Num penny, Int Num nickel, Int Num dime, Int Num quarter
    """
    penny = get_integer("How many pennies do you have?: ")
    nickel = get_integer("How many nickels do you have?: ")
    dime = get_integer("How many dimes do you have?: ")
    quarter = get_integer("How many quarters do you have?: ")
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

def data_calc(penny, nickel, dime, quarter, keepGoing=0):
    """"
    Calculates the total value of coins in a typical USD format 1.00
    :param totalValue: Int from penny*5 + nickel*5 dime*10 quarter*25
    :param totalValue: totalValue / 100
    :return: Float totalValue
    """
    totalValue = (penny * 1) + (nickel * 5) + (dime * 10) + (quarter * 25)
    totalValue = float(totalValue / 100)

    return totalValue

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