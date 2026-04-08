'''The following program asks for user input of a number and
calculates the factorial of the given number and
also validates if the given input is a number or any other type of data'''

#Take number input from the user
user_input = input("Enter a number to find its factorial: ")

# Check if input is a valid non-negative integer
if user_input.isdigit():
    num = int(user_input)
    #Mathematical calculation of factorials
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")
else:
    #To display error if the input is not a positive integer
    print("The given input is not a number. Please input a non-negative integer.")

#by Biplab Prasad Gajurel 25024641