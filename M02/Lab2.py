#***************************************************************
# Author: Kyle Noyes
# Practice: 02
# Date: 1/15/2024
# Description: This program will calculate the total value of
#   coins given
# IDE console
# Input: Float MPG var; float price var
# Output: Arithmetic sum showing the cost over 20, 75, and 500mi
# Sources: 
#***************************************************************
#START

#Hello! This program will calculate your coins total value 

#How many pennies do you have?: 55
#How many nickels do you have?: 31
#How many dimes do you have?: 3
#How many quarters do you have?: 9

#The total value of your coins is: $4.65

#END
#***************************************************************

penny = 0
nickel = 0
dime = 0
quarter = 0

print("Hello! This program will calculate your coins total value \n")

penny = int(input("How many pennies do you have?: "))
nickel = int(input("How many nickels do you have?: "))
dime = int(input("How many dimes do you have?: "))
quarter = int(input("How many quarters do you have?: "))

totalValue = (penny * 1) + (nickel * 5) + (dime * 10) + (quarter * 25)
totalValue = float(totalValue / 100)

print("\nThe total value of your coins is: ${:.2f}".format(totalValue))