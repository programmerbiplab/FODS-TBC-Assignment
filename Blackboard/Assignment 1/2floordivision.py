'''The following program takes input of two numbers from the user and 
does mathematical operation of floor divison which means it returns the quotient
as whole number even if it has numbers after decimal, floor division disregards
float numbers and only regards integers'''

#asking for user input of first number
a=int(input("Enter the first number:"))

#asking for user input of second number
b=int(input("Enter the second number:"))

#doing the mathematical operation of floor division
division_first=a//b
division_second=b//a

#printing the processed output
print("The floor-division of first number by second number is:", division_first)
print("The floor-division of second number by first number is:", division_second)

#by Biplab Prasad Gajurel 25024641