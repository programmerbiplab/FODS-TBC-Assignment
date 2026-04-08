'''The following program takes user input of number and
finds the log base 10 value of the input number'''

#Importing math module for calculation
import math

#Taking input from the user
num = float(input("Enter a positive number: "))

#To check if the number is positive
if num > 0:
    #Calculating log base 10
    result = math.log10(num)
    print("Log base 10 of", num, "is:", result)
else:
    print("Logarithm undefined for zero or negative numbers.")

#by Biplab Prasad Gajurel 25024641