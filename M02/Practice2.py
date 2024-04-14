#***************************************************************
# Author: Kyle Noyes
# Practice: 02
# Date: 1/15/2024
# Description: This program will calculate the cost of driving
#   when given a vehicles MPG and gas price
# IDE console
# Input: Float MPG var; float price var
# Output: Arithmetic sum showing the cost over 20, 75, and 500mi
# Sources: 
#***************************************************************
#START

#Hello and welcome to this cost-of-driving calcuator.

#What is the price of gas? (Num only): 3.94
#What is the vehicle's MPG? (Num only): 34.2314 

#A 20 mile trip will cost: $2.30
#A 75 mile trip will cost: $8.63
#A 500 mile trip will cost: $57.55

#END
#***************************************************************
gasPrice = 0
miPerGal = 0

print("Hello and welcome to this cost-of-driving calcuator.")

#Inputs
gasPrice = float(input("What is the price of gas? (Num only): "))
miPerGal = float(input("What is the vehicle's MPG? (Num only): "))

#Calculations
miCost = gasPrice / miPerGal
trip20 = (miCost * 20)
trip75 = (miCost * 75)
trip500 = (miCost * 500)

#Output
print("A 20 mile trip will cost: ${:.2f}".format(trip20))
print("A 75 mile trip will cost: ${:.2f}".format(trip75))
print("A 500 mile trip will cost: ${:.2f}".format(trip500))