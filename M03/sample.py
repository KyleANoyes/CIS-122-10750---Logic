# Author:           (programmer's name)

# Sample Run:

# Gumball Estimator!
# Enter the dimensions of a cylinder jar and I will
# tell you how many gumballs it will take to fill!

# Enter cylinder diameter (inches): 7
# Enter cylinder height (inches): 10

# The jar will hold 477 gumballs!

# Goodbye!

GUMBALL_VOLUME = 0.5236 # gumball with 1" diameter
PERCENT_SOLID = .65 # percentage of cylinder that will contain solids
                    # to account for space between gumballs
PI = 3.14159265

diameter = 0.0
radius = 0.0
height = 0.0
cylinder_volume = 0.0
num_gumballs = 0

print("Gumball Estimator!")
print('Enter the dimensions of a cylinder jar and I will')
print('tell you how many 1" gumballs it will take to fill!\n')

# Inputs
diameter = float(input("Enter cylider diameter (in): "))
height = float(input("Enter cylider height (in): "))

# Calculate the radius to use in the volume formula
radius = diameter / 2.0

# Calculate the volume of cylinder = πr^2h
# Multiply cylinder volume by 64% to account for empty space
# between gumballs
cylinder_volume = (PI * radius ** 2 * height) * PERCENT_SOLID

# Calculate the number of gumballs and then truncate the decimal
# portion - we want the whole number of gumballs
num_gumballs = int(cylinder_volume / GUMBALL_VOLUME)

# Outputs
print("\nThe jar will hold", num_gumballs, "gumballs!")

print("\nGoodbye!")