'''The following program takes user input of a number and
creates a function and displays factorial of the given number and
displays the output in a proper format'''

# Defining function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Asking for user input of a number
num = int(input("Enter a number to find its factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = factorial(num)
    print(f"The factorial of {num} is: {fact}")

# By Biplab Prasad Gajurel 25024641
