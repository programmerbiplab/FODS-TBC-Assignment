'''The following program takes user input of a number
and finds out whether it is an odd number or even number and
displays the result'''

#taking user input
number=int(input("Enter a number:"))

#doing modulo division to check remainder
odd=number%2
if odd>0:
    print("The input number is ODD")
else:
    print("The input number is EVEN")

#by Biplab Prasad Gajurel 25024641