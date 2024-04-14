#***************************************************************
# Author: Kyle Noyes
# Practice: 03
# Date: 1/26/2024
# Description: This program will calculate how many gumballs
#   a given cylinder size can hold
# IDE console
# Input: Float height, Float width
# Output: Number of gumballs cylindar can hold
# Sources: 
#***************************************************************
#START

#Gumball Estimator!
#Enter the dimensions of a cylinder jar and I will
#tell you how many 1" gumballs it will take to fill!

#Enter cylider diameter (in): 5
#Enter cylider height (in): 3

#The jar will hold 73 gumballs!

#Goodbye!

#END
#***************************************************************

# gumball with 1" diameter
GUMBALL_VOLUME = 0.5236 
# percentage of cylinder that will contain solids
# to account for space between gumballs
PERCENT_SOLID = .65 
# declared pi value  
PI = 3.14159265

#Control program logic flow
def main():
    # delcarations
    diameter = 0.0
    radius = 0.0
    height = 0.0
    cylinder_volume = 0.0
    num_gumballs = 0

    # welcome message
    msg_welcome()

    # inputs
    diameter, height = get_dimm()

    # radius calc
    radius = calc_radius(diameter)

    # cyl volume calc
    cylinder_volume = cyl_volume(PI, radius, height, PERCENT_SOLID)

    # total gumball calc
    num_gumballs = gumball_total(cylinder_volume, GUMBALL_VOLUME)

    # data print & end message
    msg_end(num_gumballs)

def get_dimm():
    """"
    Output text showing max gumballs and a goodbye message
    :param num_gumballs: Int
    """
    diameter = float(input("Enter cylider diameter (in): "))
    height = float(input("Enter cylider height (in): "))
    return diameter, height

def msg_welcome():
    """"
    Input text welcoming user to this program
    """
    print("Gumball Estimator!")
    print('Enter the dimensions of a cylinder jar and I will')
    print('tell you how many 1" gumballs it will take to fill!\n')

def msg_end(num_gumballs):
    """"
    Output text showing max gumballs and a goodbye message
    :param num_gumballs: Int
    """
    print("\nThe jar will hold", num_gumballs, "gumballs!")
    print("\nGoodbye!")

def calc_radius(diameter):
    """"
    Calculates the radius from diameter
    :param  radius: Float, diameter / 2 to get radius
    :return: Float, radius
    """
    radius = diameter / 2.0
    return radius

def cyl_volume(PI, radius, height, PERCENT_SOLID):
    """"
    Calculates the volume of our cylinder
    :param  cylinder_volume: Float, calculation of cylinder volume
    :return: Float, cylinder_volume
    """
    cylinder_volume = (PI * radius ** 2 * height) * PERCENT_SOLID
    return cylinder_volume

def gumball_total(cylinder_volume, GUMBALL_VOLUME):
    """"
    Calculates the total number of gumballs
    :param num_gumballs: Int, Calculated from cylinder_volumes / gumball_volume
    :return: Int, num_gumballs value
    """
    num_gumballs = int(cylinder_volume / GUMBALL_VOLUME)
    return num_gumballs

main()