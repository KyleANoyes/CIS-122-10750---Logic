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
        coinCount = 0
        totalValue = 0
    
        # Input / construct object
        balance = user_input()

        # Validate program inputs are valid
        dataInvalid = data_validate(balance)

        # If data valid, continue; if invalid, terminate program
        if len(dataInvalid.__str_invalid__()) == 0:
                coinCount = count_coins(balance)
                totalValue = data_calc(balance)
                msg_end(coinCount, totalValue)

        else:
            # Terminate program, alert user to which variable(s) broke
            print(msg_error())
            print(dataInvalid.__str_invalid__())
        
        keepGoing = msg_continue()


class balance:
    """
    Class balance
        Holds the coins the user inputs
    """
    # Init values
    __penny__ = 0
    __nickel__ = 0
    __dime__ = 0
    __quarter__ = 0

    # Constructor class
    def __init__(self, p, n, d, q):
        self.__penny__ = p
        self.__nickel__ = n
        self.__dime__ = d
        self.__quarter__ = q
    
    # Setters
    """
    Function to set pennies
    """
    def set_penny(self, p):
        self.__penny__ = p
    
    """
    Function to set nickels
    """
    def set_nickel(self, n):
        self.__nickel__ = n

    """
    Function to set dimes
    """
    def set_dime(self, d):
        self.__dime__ = d

    """
    Function to set quarters
    """
    def set_quarter(self, q):
        self.__quarter__ = q

    # Getters
    """
    Function to retrieve pennies
    """
    def get_penny(self):
        return self.__penny__
    
    """
    Function to retrieve nickels
    """
    def get_nickel(self):
        return self.__nickel__

    """
    Function to retrieve dimes
    """
    def get_dime(self):
        return self.__dime__

    """
    Function to retrieve quarters
    """
    def get_quarter(self):
        return self.__quarter__
    
    # Return string representation
    """
    This function will return this objects properties as a string.
    This particular one is to return every value
    """
    def __str__(self):
        return "Pennies: {}, \
                Nickels: {}, \
                Dimes {}, \
                Quarters {}".format(self.__penny__,
                                    self.__nickel__,
                                    self.__dime__,
                                    self.__quarter__)
    

class invalid_data:
    """
    Class invalid_data
        Invalid coin amounts added here and passed around
    """
    invalPenny = 0
    invalNickel = 0
    invalDime = 0
    invalQuarter = 0

    # using "i" prefix to avoid var name overlap with balance class
    #     Also helps me organize my thoughts, i is "invalid"

    # Constructor
    """
    Function to initialize object with inval penny/nickel/dime/quarter
    """
    def __init__(self, iP, iN, iD, iQ):
        self.__invalPenny__ = iP
        self.__invalNickel__ = iN
        self.__invalDime__ = iD
        self.__invalQuarter__ = iQ

    # setters
    """
    Function to set invalid pennies
    """
    def set_invalPenny(self, iP):
        self.__invalPenny__ = iP
    
    """
    Function to set invalid nickels
    """
    def set_invalNickel(self, iN):
        self.__invalNickel__ = iN

    """
    Function to set invalid dimes
    """
    def set_invalDime(self, iD):
        self.__invalDime__ = iD

    """
    Function to set invalid quarters
    """
    def set_invalQuarter(self, iQ):
        self.__invalQuarter__ = iQ

    # Getters
    """
    Function to retrieve invalid pannies
    """
    def get_invalPenny(self):
        return self.__invalPenny__
    
    """
    Function to retrieve invalid nickels
    """
    def get_invalNickel(self):
        return self.__invalNickel__

    """
    Function to retrieve invalid dimes
    """
    def get_invalDime(self):
        return self.__invalDime__
    
    """
    Function to retrieve invalid quarters
    """
    def get_invalQuarter(self):
        return self.__invalQuarter__

    # String return all
    """
    This function will return this objects properties as a string.
    This particular one is to return every value
    """
    def __str_all__(self):
        return "Invalid pennies: {}, \
                Invalid Nickels: {}, \
                Invalid Dimes {}, \
                Invalid Quarters {}".format(self.get_invalpenny(),
                                            self.get_invalnickel(),
                                            self.get_invaldime(),
                                            self.get_invalquarter())

    # String return only error
    """
    This function will return this objects properties as a string.
    This one constructs an error msg with only invalid coins
    return invalList
    """
    def __str_invalid__(self):
        invalList = ""

        # Construct the invalid list
        if self.get_invalPenny() < 0:
            invalList += "\nInvalid pennies: " + str(self.get_invalPenny()) + "\n"
        if self.get_invalNickel() < 0:
            invalList += "\nInvalid nickels: " + str(self.get_invalNickel()) + "\n"
        if self.get_invalDime() < 0:
            invalList += "\nInvalid dimes: " + str(self.get_invalDime()) + "\n"
        if self.get_invalQuarter() < 0:
            invalList += "\nInvalid quarters: " + str(self.get_invalQuarter()) + "\n"

        return invalList



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


def msg_error():
    """"
    Displays a simple error message. Can be easily edited
    """
    return "\nOne or more coins are less than zero. Please restart this program."


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


def user_input():
    """"
    Gets user num of coins and stores values as integers
    :param coins: List, begins empty and then is appended to
    :return: List, coins
    """
    coins = []
    coins.append(get_integer("How many pennies do you have?: "))
    coins.append(get_integer("How many nickels do you have?: "))
    coins.append(get_integer("How many dimes do you have?: "))
    coins.append(get_integer("How many quarters do you have?: "))

    return balance(coins[0], coins[1], coins[2], coins[3])


def data_validate(balance):
    """"
    Validates if we have any bad data, check if less than zero
    :param coins: list, contains inputed values from user
    :param dataInvalid: list, appendeds offending var name if value < 0
    :return: list, dataInvalid
    """
    invalidInput = invalid_data(0, 0, 0, 0)
    if balance.get_penny() < 0:
        invalidInput.set_invalPenny(balance.get_penny())
    
    if balance.get_nickel() < 0:
        invalidInput.set_invalNickel(balance.get_nickel())
    
    if balance.get_dime() < 0:
        invalidInput.set_invalDime(balance.get_dime())
    
    if balance.get_quarter() < 0:
        invalidInput.set_invalQuarter(balance.get_quarter())

    return invalidInput


def data_calc(balance):
    """"
    Calculates the total value of coins in a typical USD format 1.00
    :param balance: Object, contains user inputed quantities of coins
    :param totalValue: Int from penny*5 + nickel*5 dime*10 quarter*25
    :param totalValue: totalValue / 100
    :return: Float totalValue
    """
    totalValue = (balance.get_penny() * 1) + \
                 (balance.get_nickel() * 5) + \
                 (balance.get_dime() * 10) + \
                 (balance.get_quarter() * 25)
    
    totalValue = float(totalValue / 100)

    return totalValue


def count_coins(balance):
    """"
    Adds together total number of coins, it's a fun For loop
    :param coins: List, contains user inputed quantities of coins
    :param coinCount: Int, added total of all nums in list coins
    :return: Int, coinCount
    """
    coinCount = 0

    coinCount += balance.get_penny()
    coinCount += balance.get_nickel()
    coinCount += balance.get_dime()
    coinCount += balance.get_quarter()

    
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