#***************************************************************
# Author: Kyle Noyes
# Practice: 09
# Date: 03/10/2024
# Description: This program will create resturant objects
# Input: Resturant Name, Food specialty, price, and rating
# Output: A resturants various components of object
#***************************************************************

"""
Welcome to my Resturant creation program!

Please enter the resturant info for resturant #1
Please enter the resturant title: A good place
Please enter the resturant food type: Good food
Please enter the price range ($, $$, $$$, or $$$$): $$$
Please enter the resturant rating (1 - 5): 4

Resturant            Specialty            Price Range          Rating
---------            ---------            -----------          ------
A good place         Good food            $$$                  4

Would you like to generate another resturant? (y/n): y

Please enter the resturant info for resturant #2
Please enter the resturant title: An awful resturant
Please enter the resturant food type: Gross food
Please enter the price range ($, $$, $$$, or $$$$): $
Please enter the resturant rating (1 - 5): 1

Resturant            Specialty            Price Range          Rating
---------            ---------            -----------          ------
An awful resturant   Gross food           $                    1

Would you like to generate another resturant? (y/n): n

Thank you for using my program!
"""

import valid

class Resturant:
    """
    Class Resturant
    """
    __title__ = ""
    __foodType__ = ""
    __price_range__ = ""
    __rating__ = ""

    """
    Function to initialize object with title, food, price, and rating
    """
    def __init__(self, t, f, p, r):
        self.__title__ = t
        self.__foodType__ = f
        self.__price_range__ = p
        self.__rating__ = r
    
    # Getters
    """
    Function to read the object's title
    """
    def get_title(self):
        return self.__title__

    """
    Function to read the object's specialty
    """
    def get_food_type(self):
        return self.__foodType__

    """
    Function to read the object's price
    """
    def get_price_range(self):
        return self.__price_range__
    
    """
    Function to read the object's rating
    """
    def get_rating(self):
        return self.__rating__
    

    # Setters
    """
    Function to set title equal to user input
    """
    def set_title(self, t):
        self.__title__ = t
    
    """
    Function to set food specialty equal to user input
    """
    def set_food_type(self, f):
        self.__foodType__ = f

    """
    Function to set price range equal to user input
    """
    def set_price_range(self, p):
        self.__price_range__ = p

    """
    Function to set rating equal to user input
    """
    def set_rating(self, r):
        self.__rating__ = r


def main():
    """
    Main fucntion handling data exchanges between other functions
    :param i: Int, used to track number of resturant creations
    :param termProgram: Bool, adjusted if user wants to end program
    :param userInput: String, holds the y/n response
    :param resturant: Object, holds the resturant created data
    """
    i = 0
    termProgram = False
    userInput = ""
    message_list(0)

    while termProgram != True:
        i += 1

        message_list(3, "#{}".format(i))
        resturant = construct_resturant()
        print_resturant(resturant)

        userInput = valid.get_y_or_n("Would you like to generate another resturant? (y/n): ")

        if userInput == "n":
            termProgram = True

    message_list(4)


def construct_resturant():
    """
    Main class consttructor. Can be called more than once
        so needs to live in own function
    :param title: String, title of resturant
    :param foodType: String, food specialty of resturant
    :param priceRange: String, the $$$ evaluator of price
    :rating: Int, the rating of the resturant 1 - 5

    return Resturant object
    """
    title = ""
    foodType = ""
    priceRange = ""
    rating = 0

    title = valid.get_string("Please enter the resturant title: ")
    foodType = valid.get_string("Please enter the resturant food type: ")
    priceRange = price_range_valid()
    rating = rating_valid()

    return Resturant(title, foodType, priceRange, rating)


def message_list(code="", misc=""):
    """
    Functain containing commonly referenced strings
    :param code: Int, used to choose specific message to display
    """
    if code == 0:
        print("Welcome to my Resturant creation program!")
    elif code == 1:
        print("Input is invlaid, please only enter $, $$, $$$, or $$$$\n")
    elif code == 2:
        print("Rating can not be less than 1 or greater than 5\n")
    elif code == 3:
        print("\nPlease enter the resturant info for resturant {}".format(misc))
    elif code == 4:
        print("\nThank you for using my program!")
    else:
        print("Invalid code entered. Please alert the programmer")


def price_range_valid():
    """
    Checks if user supplied data is valid for the $$$ price range
        There is a lot of nested loop logic here... gross
    :param invalidData: Bool, updated if bad data found 
    :param priceRange: String, Contains the $ strings

    return priceRange
    """
    invalidData = True
    priceRange = ""

    while invalidData == True:
        invalidData = False

        priceRange = valid.get_string("Please enter the price range ($, $$, $$$, or $$$$): ")
        if len(priceRange) > 0 and len(priceRange) < 4:
            for i in range(len(priceRange)):
                if priceRange[i] != "$":
                    invalidData = True
        else:
            invalidData = True
        
        if invalidData == True:
            message_list(1)
    
    return priceRange


def rating_valid():
    """
    Checks if user supplied data is valid between ints 1 - 5
    :param invalidData: Bool, updated if bad data found 
    :param rating: Int, Contains the user rating

    return rating
    """
    invalidData = True
    rating = 0

    while invalidData == True:
        invalidData = False

        rating = valid.get_integer("Please enter the resturant rating (1 - 5): ")

        if rating < 1 or rating > 5:
            message_list(2)
            invalidData = True
    
    return rating


def print_resturant(resturant):
    """
    Output of the resturant data on update
    :param resturant: Created object and attributes
    """
    print("\n{: <20} {: <20} {: <20} {: <20}".format("Resturant", 
                                              "Specialty", 
                                              "Price Range", 
                                              "Rating"))
    print("{: <20} {: <20} {: <20} {: <20}".format("---------", 
                                            "---------", 
                                            "-----------", 
                                            "------"))
    print("{: <20} {: <20} {: <20} {: <20}\n".format(resturant.get_title(), 
                                              resturant.get_food_type(), 
                                              resturant.get_price_range(), 
                                              resturant.get_rating()))


main()