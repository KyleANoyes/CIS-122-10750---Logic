#***************************************************************
# Author: Kyle Noyes
# Practice: 08
# Date: 03/02/2024
# Description: This program will calculate election results
# Input: Str, candidate name; Int, candidate votes; Str, continue
# Output: Results of the election and individual winners stats
#***************************************************************

""" 
Hello! Welcome to this election calculator
Enter candidates' names and the number to votes they recieved
to get the winner.

Please enter the candidates name:
Please enter a string: yElLoW

Please enter the candidates vote:
Please enter an integer: 491

Would you like to add another candidates results? (y/n):
Please enter 'y' or 'n': y
Please enter the candidates name:
Please enter a string: red

Please enter the candidates vote:
Please enter an integer: 947

Would you like to add another candidates results? (y/n):
Please enter 'y' or 'n': y
Please enter the candidates name:
Please enter a string: ORANGE

Please enter the candidates vote:
Please enter an integer: 1347

Would you like to add another candidates results? (y/n):
Please enter 'y' or 'n': y
Please enter the candidates name:
Please enter a string: yellow

Please enter the candidates vote:
Please enter an integer: 194

Would you like to add another candidates results? (y/n):
Please enter 'y' or 'n': n

Results:
Candidate, votes, '%' votes
----------------------------------
Yellow    685    22.99
Red    947    31.79
Orange    1347    45.22

The winnder is: Orange

Thank you for using my program!
"""

def main():
    """
    The main controlling body of this program.
    :param candName: List, candidate names
    :param candVote: List, candidate votes
    :param candPerc: List, candidate percentage win
    :param win: Str, contains the name of the winner
    :param newInput: Str, used to check if user wants to add more
    :param duplicate: Int, used for tracking duplicate data
    """
    candName = []
    candVote = []
    candPerc = []
    newInput = "y"
    win = ""

    message_list(0)

    while newInput != "n":
        # Reset key data values
        userInput = []
        duplicate = -1

        # Normalize user data
        message_list(1)
        userInput.append(get_string().lower())
        message_list(2)
        userInput.append(get_integer())

        # Check for duplicate data
        duplicate = check_dup(userInput, candName)

        # Merge of create new data
        if duplicate != -1:
            candVote = merge_dup(userInput, candVote, duplicate)
        else:
            candName, candVote = new_cand(userInput, candName, candVote)

        message_list(3)

        newInput = get_y_or_n()
    
    candPerc, win = calc_result(candName, candVote, candPerc)

    display_result(candName, candVote, candPerc, win)

    message_list(4)


def message_list(msgCode=""):
    """
    Functain containing commonly referenced strings
    :param msgCode: Int, used to choose specific message to display
    """
    if msgCode == 0:
        print("Hello! Welcome to this election calculator")
        print("Enter candidates' names and the number to votes they recieved")
        print("to get the winner.\n")
    elif msgCode == 1:
        print("Please enter the candidates name: ")
    elif msgCode == 2:
        print("\nPlease enter the candidates vote: ")
    elif msgCode == 3:
        print("\nWould you like to add another candidates results? (y/n): ")
    elif msgCode == 4:
        print("\nThank you for using my program!")
    elif msgCode == 5:
        print("\nResults: ")
        print("Candidate, votes, '%' votes")
        print("----------------------------------")
    else:
        print("Unknown error")
    


def check_dup(userInput, candName):
    """
    Checks for duplicate data on input
    :param userInput: List, contains user entered data
    :param candName: List, candidate names 
    :param duplicate: Int, used to track index where dup is found

    return duplicate
    """
    duplicate = -1

    for i in range(len(candName)):
        if userInput[0] == candName[i]:
            duplicate = i
        else:
            pass

    return duplicate


def merge_dup(userInput, candVote, duplicate):
    """
    This function will merge diplicate vote data
    :param userInput: List, contains user entered data
    :param candVote: List, candidate votes
    :param duplicate: Int, index of duplication found

    return candVote
    """
    candVote[duplicate] += userInput[1]

    return candVote


def new_cand(userInput, candName, candVote):
    """
    This function adds a new candidate to the candidate list
        and adds their total votes
    :param userInput: List, contains user entered data
    :param candName: List, candidate names
    :param candVote: List, candidate votes

    return candName, candVote
    """
    candName.append(userInput[0])
    candVote.append(userInput[1])

    return candName, candVote


def calc_result(candName, candVote, candPerc):
    """
    This function does all the funky calculations and determination
        for who has won the election.
    :param candName: List, candidate names.
    :param candVote: List, candidate votes
    :param candPerc: List, empty, but will contain percentage win
    :param totalVotes: Int, Add total of votes
    :param maxVote: Int, shows index with greatest vote count
    :param maxVoteIndex: Int, identifies index of greatest vote
    :param win: Str, contains candidates name with greatest vote

    return candPerc, win
    """
    totalVotes = 0
    maxVote = 0
    maxVoteIndex = 0
    win = ""

    for i in range(len(candVote)):
        totalVotes += candVote[i]

        if candVote[i] > maxVote:
            maxVote = candVote[i]
            maxVoteIndex = i

    for i in range(len(candVote)):
        candPerc.append((candVote[i] / totalVotes) * 100)
    
    win = candName[maxVoteIndex]
    
    return candPerc, win


def display_result(candName, candVote, candPerc, win):
    """
    Function to display results. Too complex for message handler function
    :param candName: List, candidate names
    :param candVote: List, candidate votes
    :param candPerc: List, candidate percentage win
    :param win: Str, contains the name of the winner
    """
    message_list(5)

    for i in range(len(candName)):
        print("{}    {}    {:0.2f}".format(candName[i].capitalize(), candVote[i], candPerc[i]))

    print("\nThe winnder is: {}".format(win.capitalize()))


# -- imported user get functions -- #
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
# --------------------------------- #

main()