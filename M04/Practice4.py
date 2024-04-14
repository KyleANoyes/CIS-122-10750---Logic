#***************************************************************
# Author: Kyle Noyes
# Practice: 04
# Date: 1/29/2024
# Description: This program will calculate the amount of change
#   needed for given collective coin value
# IDE console
# Input: INT penny, INT nickel, INT dime, INT quarter, INT dollar
# Output: largest denominations of change for given input
# Sources: 
#***************************************************************
#START

# Hello! Welcome to this change calculator

# Please enter the needed change value as a whole number
# such as 167 for $1.67 or 37 for $0.37: 597

# 5 Dollars
# 3 Quarters
# 2 Dimes
# 2 Pennies

# Thank you for using my change calculator!!

#END
#***************************************************************

def main():
    # var declaration
    penny = 0
    nickel = 0
    dime = 0
    quarter = 0
    dollar = 0
    userInput = 0
    msgOutput = "\n"

    # Display welcome message
    msg_start()

    # Get user input
    userInput = get_input()

    # Send user input to calc function; save results
    dollar, quarter, dime, nickel, penny = calc_coins(userInput)

    # Construct the final message with proper grammar & w/o speling mistakes
    msgOutput = msg_plural(dollar, quarter, dime, nickel, penny, msgOutput)

    # Display constructed change output + bye
    msg_end(msgOutput)


def msg_start():
    """"
    Displays a happy welcome message. That is all :)
    """
    print("\nHello! Welcome to this change calculator\n")

def msg_plural(dollar, quarter, dime, nickel, penny, msgOutput):
    """"
    Checks if input requires pluralization or not. Constructs output msg
    :param penny: int, number of pennies
    :param nickel: int, number of nickles
    :param dime: int, number of dimes
    :param quarter: int, number of quarters
    :param dollar: int, number of quarters
    :param msgOutput: string, constructed string for all number configs
    :return: string, final constructed message to display change
    """
    if dollar > 1:
        msgOutput = msgOutput + "{} Dollars\n".format(dollar)
    elif dollar == 1:
        msgOutput = msgOutput + "{} Dollar\n".format(dollar)
    else:
        pass # using pass for readability. Closes the logic loop

    if quarter > 1:
        msgOutput = msgOutput + "{} Quarters\n".format(quarter)
    elif quarter == 1:
        msgOutput = msgOutput + "{} Quarter\n".format(quarter)
    else:
        pass

    if dime > 1:
        msgOutput = msgOutput + "{} Dimes\n".format(dime)
    elif dime == 1:
        msgOutput = msgOutput + "{} Dime\n".format(dime)
    else:
        pass

    if nickel > 1:
        msgOutput = msgOutput + "{} Nickles\n".format(nickel)
    elif nickel == 1:
        msgOutput = msgOutput + "{} Nickle\n".format(nickel)
    else:
        pass

    if penny > 1:
        msgOutput = msgOutput + "{} Pennies\n".format(penny)
    elif penny == 1:
        msgOutput = msgOutput + "{} Penny\n".format(penny)
    else:
        pass

    # This will catch whacky edge cases. Otherwise output is blank
    if msgOutput == "\n":
        msgOutput = "\nNo change needed.\n"

    return msgOutput
    

def msg_end(msgOutput):
    """"
    Displays the final messages
    :param msgOutput: string, constructed string of change amounts
    print goodbye message
    """
    print(msgOutput)
    print("Thank you for using my change calculator!!\n")


def get_input():
    """"
    Gets user input
    print instructions for expected value. Change as int not float
    :param userInput: int, gets the combined coin value to be parsed
    return: int, userInput with combined value
    """
    print("Please enter the needed change value as a whole number")
    userInput = int(input("such as 167 for $1.67 or 37 for $0.37: "))
    return userInput


def calc_coins(userInput):
    """"
    Gets greatest denomination from largest to smallest.
        Also checks if val > 0 to not give negative change.
    :param dollar: int, greatest denomination of dollars
    :param quarter: int, greatest denomination of quarters
    :param dime: int, greatest denomination of dimes
    :param nickel: int, greatest denomination of nickels
    :param penny: int, greatest denomination of pennies 
    return: int, userInput with combined value
    """
    if userInput > 0:
        dollar = userInput // 100
        userInput = userInput % 100
        
        quarter = userInput // 25
        userInput = userInput % 25
        
        dime = userInput // 10
        userInput = userInput % 10

        nickel = userInput // 5
        userInput = userInput % 5

        penny = userInput
    
    else:
        dollar = 0
        quarter = 0
        dime = 0
        nickel = 0
        penny = 0

    return "a", "data", "AAFA", "ujrtzz", "5", 

main()