# Hello! Welcome to my statistics program.

# Type the word "calc" to begin the calculation of inputs

# Please enter a number to add to the list: 5
# Last value entered: 5

# Please enter a number to add to the list: 10
# Last value entered: 10

# Please enter a number to add to the list: 15
# Last value entered: 15

# Please enter a number to add to the list: c

# The sum of your numbers: 30

# The average of your numbers: 10.0

# The smallest number in the set: 5

# The largest number in the set: 15

# Would you like to re-run this program?
# Please enter 'y' or 'n': y

# Type the word "calc" to begin the calculation of inputs

# Please enter a number to add to the list: 9
# Last value entered: 9

# Please enter a number to add to the list: ü
# Input was invalid. Please try again.

# Please enter a number to add to the list: 2
# Last value entered: 2

# Please enter a number to add to the list: c

# The sum of your numbers: 11

# The average of your numbers: 5.5

# The smallest number in the set: 2

# The largest number in the set: 9

# Would you like to re-run this program?
# Please enter 'y' or 'n': n

# Thank you for using my program!

#-------------------------------------------------------------#

def main():
    """
    Function that acts as the main controller for data handling / movement
    :param userInpt: List, will be used to move large quantities of data
    :param keepGoing: Bool, used as bool for checking loop conditions
    :param dataSum: Int or Float, the sum
    :param dataAvg: Int or Float, the avg
    :param dataMin: Int or Float, the sin
    :param dataMax: Int or Float, the max
    """
    userInput = []
    keepGoing = False
    dataSum = 0
    dataAvg = 0
    dataMin = 0
    dataMax = 0

    msg_list(0)

    msg_list(1)
    while keepGoing != True:
        userInput.append(get_user_input("str", "a number to add to the list"))

        try:
            userInput[-1] = int(userInput[-1])
            if data_valid(userInput[-1], "int") == True:
                msg_list(3, userInput[-1])
            else:
                msg_list(2)
                # purges the last indexed element since we used .append earlier
                # This should never be reached, but is good error handling.
                userInput = userInput[0:-1]
        except:
            if userInput[-1][0].lower() != "c":
                userInput = userInput[0:-1]
                msg_list(2)
            else:
                userInput = userInput[0:-1]
                keepGoing = True

    dataSum = get_sum(userInput)
    dataAvg = get_avg(userInput)
    dataMin = get_min(userInput)
    dataMax = get_max(userInput)

    msg_display_calc(dataSum, dataAvg, dataMin, dataMax)

    keepGoing = msg_continue()

    if keepGoing == True:
        main()
    else:
        msg_list(5)
    

def msg_list(message="", misc=""):    
    """
    Function to print various messages to the user
    :param message: Str, indicates code to search for or enter custom msg.
    :param dataAvg: Str, substitue text that can be added to 2 part messages
    """
    if message == 0:
        print("\nHello! Welcome to my statistics program.")
    elif message == 1:
        print("\nType the word \"calc\" to begin the calculation of inputs\n")
    elif message == 2:
        print("Input was invalid. Please try again.\n")
    elif message == 3:
        print("Last value entered: {}\n".format(misc))
    elif message == 4:
        print("Calculations beginning\n")
    elif message == 5:
        print("\nThank you for using my program!\n")
    else:
        print("\n")

def msg_display_calc(dataSum, dataAvg, dataMin, dataMax):
    """
    Function to print the final data to the user
    :param dataSum: Int or Float, the sum
    :param dataAvg: Int or Float, the avg
    :param dataMin: Int or Float, the sin
    :param dataMax: Int or Float, the max
    """
    print("\nThe sum of your numbers: {}\n".format(dataSum))
    print("The average of your numbers: {}\n".format(dataAvg))
    print("The smallest number in the set: {}\n".format(dataMin))
    print("The largest number in the set: {}".format(dataMax))


def msg_continue(keepGoing=0):
    """"
    Repeat message and handler for related data
    :param keepGoing: int, boolean stand-in for returned true/false
    :return: Int keepGoing as 0 or 1
    """
    print("\nWould you like to re-run this program?")
    if get_y_or_n() == "y":
        keepGoing = True
    else:
        keepGoing = False

    return keepGoing


def get_sum(userInput):
    """
    Function to get the sum of a list
    :param userInput: List, contains all data to check
    :param calc: Int or Float, summation of list; avg of list
    :return: Int or Float, avg number
    """
    calc = 0

    for i in range(len(userInput)):
        calc = calc + userInput[i]

    return calc


def get_avg(userInput):
    """
    Function to find avg value in list
    :param userInput: List, contains all data to check
    :param calc: Int or Float, summation of list; avg of list
    :return: Int or Float, avg number
    """
    calc = 0

    for i in range(len(userInput)):
        calc = calc + userInput[i]

    calc = calc / len(userInput)

    return calc


def get_max(userInput):
    """
    Function to find minimum value in list
    :param userInput: List, contains all data to check
    :param man: Int or Float, used to store largest num
    :return: Int or Float, largest number in list
    """
    max = userInput[0]

    for i in range(len(userInput)):
        if userInput[i] > max:
            max = userInput[i]

    return max


def get_min(userInput):
    """
    Function to find minimum value in list
    :param userInput: List, contains all data to check
    :param min: Int or Float, used to store minimum num
    :return: Int or Float, smallest number in list
    """
    min = userInput[0]

    for i in range(len(userInput)):
        if userInput[i] < min:
            min = userInput[i]

    return min


def get_user_input(inputType, printMsg="data"):
    """
    Function to prompt for the user to enter a specific data type
    :param inputType: Str, used to selec input type condition
    :param printMsg: Str, custom message display to user
    :param userInput: Str, used to store and return inputted data
    :param valid: Bool, used to ensure loop completes with valid input
    :return: Str, int, or float. Contains users data
    """
    userInput = ""
    valid = False

    while valid != True:
        try:
            if inputType == "str":
                userInput = str(input("Please enter {}: ".format(printMsg)))
            elif inputType == "int":
                userInput = int(input("Please enter {}: ".format(printMsg)))
            elif inputType == "float":
                userInput = float(input("Please enter {}: ".format(printMsg)))
            else:
                pass
            valid = True
        except:
            msg_list[2]

    return userInput


def get_y_or_n(prompt="Please enter 'y' or 'n': "):
    """
    Function to prompt for and return 'y' or 'n'.
    'Y', 'N', and all cases of 'yes' and 'no' are accepted.
    :param prompt: string Optional string to use as prompt
    :return: string Non-empty string of characters
    """
    answer = ""
    answer = input(prompt)
    answer = answer[0].lower()

    while answer != "n" and answer != "y":
        print("Invalid response.")
        answer = input(prompt)
        answer = answer.lower()

    return answer

def data_valid(dataCheck, typeCheck, boolCheck=0):
    """"
    Internal data validation tool
    :param dataCheck: Function Parameter, data to be checked
    :param typeCheck: Function Parameter, specify data comparison type
    :param boolCheck: Int, retainer for Bool check result
    :return: boolCheck as True / False / 2
    """

    if typeCheck == "int":
        try:
            if (dataCheck % 1) == 0:
                boolCheck = True
            else:
                boolCheck = False
        except:
            boolCheck = 0

    if typeCheck == "float":
        try:
            # Checks if we have a decimal. Complex, but it's a good istype() substitute
            # the str compare is not great... but it works and is easy to read
            if (dataCheck % 1) > 0 and (dataCheck % 1) < 1:
                boolCheck = True
            elif (str(dataCheck % 1) == "0.0"):
                boolCheck = True
            else:
                boolCheck = False
        except:
            boolCheck = 0

    if typeCheck == "string":
        try:
            dataCheck + "Hello world :)"
            boolCheck = True
        except:
            boolCheck = 0

    return boolCheck

main()