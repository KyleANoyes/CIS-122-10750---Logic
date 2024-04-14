import valid as v

# Welcome to PCC Credit Union

# 1. View balance
# 2. Make deposit
# 3. Withdraw funds
# 4. Quit

# Enter choice: 2
# Enter deposit amount $ 954
# You are depositing: $954.00

# 1. View balance
# 2. Make deposit
# 3. Withdraw funds
# 4. Quit

# Enter choice: 3
# Enter withdraw amount $ 94.4876
# You are withdrawing: $94.49

# 1. View balance
# 2. Make deposit
# 3. Withdraw funds
# 4. Quit

# Enter choice: 1
# Account balance: $ 859.51

# 1. View balance
# 2. Make deposit
# 3. Withdraw funds
# 4. Quit

# Enter choice: 4

# Thank you for using PCC Credit Union!


QUIT = 4


def main():
    balance = 0.0
    userInputFloat = 0
    userInputInt = 0
    userInputStr = ""
    eval = False


    print("Welcome to PCC Credit Union")

    while userInputInt != QUIT:
        #Introduction
        print_menu()

        #Get user input choice
        userInputInt = v.get_integer("\nEnter choice: ")

        # Evaluate user choice, enter matching condition
        if userInputInt == 1:
            view_balance(balance)
        elif userInputInt == 2:
            userInputFloat = get_deposit_amt()
            balance = balance + userInputFloat

        elif userInputInt == 3:
            userInputFloat = get_withdraw_amt()
            balance = balance - userInputFloat

        elif userInputInt == 4:
            pass
        else:
            print(error_code(1))

    print("\nThank you for using PCC Credit Union!")


def get_deposit_amt(eval=False):
    while eval == False:
        userInputFloat = v.get_real("Enter deposit amount $ ")
        eval = is_pos(userInputFloat)
        if eval == True:
            print("You are depositing: ${:.2f}".format(userInputFloat))
        else:
            print(error_code(2))

    return userInputFloat


def get_withdraw_amt(eval=False):
    while eval == False:
        userInputFloat = v.get_real("Enter deposit amount $ ")
        eval = is_pos(userInputFloat)
        if eval == True:
            print("You are withdrawing: ${:.2f}".format(userInputFloat))
        else:
            print(error_code(2))

    return userInputFloat


def get_input(inputType, displayMsg="", eval=False):
    if inputType == "str":
        while eval != True:
            try:
                userData = input(displayMsg)
                eval = is_string(userData)
            except:
                print(error_code(0))

    if inputType == "int":
        while eval != True:
            try:
                userData = int(input(displayMsg))
                eval = is_int(userData)
            except:
                print(error_code(0))

    if inputType == "float":
        while eval != True:
            try:
                userData = float(input(displayMsg))
                eval = is_float(userData)
            except:
                print(error_code(0))
    
    return userData


def error_code(errorCondition):
    """
    Function to centralize error messages
    :param errorCondition: Int, used to call specific error condition text
    :param errorMsg: Str, pre-defined string related to specified error condition
    :return: Str, the error message... which is not good :(
    """
    if errorCondition == 0:
        errorMsg = "Invalid input."
    elif errorCondition == 1:
        errorMsg = "Choice was invalid. Please enter a 1, 2, or 3. Enter 4 to quit."
    elif errorCondition == 2:
        errorMsg = "Input can not be a negative number. Please enter a positive number or 0 to end transaction"
    elif errorCondition == 3:
        errorMsg = "Input can not be a positive number. Please enter a negative number or 0 to end transaction"
    else:
        errorMsg = "An unknown error has occoured. Please alert the programmer"
    
    return errorMsg


## Below is my validation methodology ##

def is_yes_no(inputData, eval=False):
    """
    Function to check if user entered a yes or a no
    :param inputData: undefined (inherited type), var to be evaluated
    :param eval: Boolean, host the evaulation of the inputData variable
    :return: Boolean, eval
    """
    if inputData[0] == "y" or inputData[0] == "Y":
        eval = True
    elif inputData[0] == "n" or inputData[0] == "N":
        eval = True
    else:
        eval = False

    return eval


def is_string(inputData, eval=False):
    """
    Function to check if data is a string
    :param inputData: undefined (inherited type), var to be evaluated
    :param eval: Boolean, host the evaulation of the inputData variable
    :return: Boolean, eval
    """
    try:
        inputData + "Hello world :)"
        eval = True
    except:
        eval = False
    
    return eval


def is_int(inputData, eval=False):
    """
    Function to check if data is an integer
    :param inputData: undefined (inherited type), var to be evaluated
    :param eval: Boolean, host the evaulation of the inputData variable
    :return: Boolean, eval
    """
    try:
        if (inputData % 1) == 0:
            eval = True
        else:
            eval = False
    except:
        pass

    return eval


def is_float(inputData, eval=False):
    """
    Function to check if data is a float
    :param inputData: undefined (inherited type), var to be evaluated
    :param eval: Boolean, host the evaulation of the inputData variable
    :return: Boolean, eval
    """
    try:
        if (inputData % 1) > 0 and (inputData % 1) < 1:
            eval = True
        elif (str(inputData % 1) == "0.0"):
            eval = True
        else:
            eval = False
    except:
        eval = False
    
    return eval


def is_pos(inputData, eval=False):
    """
    Function to check if data is positive 
    :param inputData: undefined (inherited type), var to be evaluated
    :param eval: Boolean, host the evaulation of the inputData variable
    :return: Boolean, eval
    """
    try:
        if inputData >= 0:
            eval = True
        else:
            eval = False
    except:
        eval = False
    
    return eval


def is_neg(inputData, eval=False):
    """
    Function to check if data is Negative 
    :param inputData: undefined (inherited type), var to be evaluated
    :param eval: Boolean, host the evaulation of the inputData variable
    :return: Boolean, eval
    """
    try:
        if inputData <= 0:
            eval = True
        else:
            eval = False
    except:
        eval = False
    
    return eval

########################################


def print_menu():
    """
    Function to print the menu to view balance, make deposit, or withdraw funds
    :return: none
    """
    print("\n1. View balance")
    print("2. Make deposit")
    print("3. Withdraw funds")
    print("4. Quit")


def view_balance(balance):
    """
    Function to print current account balance.
    :param balance: float, current account balance
    :return: none
    """
    print("Account balance: $", format(balance, ".2f"))


main()