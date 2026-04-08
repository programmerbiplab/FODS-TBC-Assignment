'''The following program creates seperate functions for the
respective arithmetic calculations and prints the required
output of the defined arithmetic functions'''

# I. Addition
def add(a, b):
    return a + b

# II. Subtraction
def subtract(a, b):
    return a - b

# III. Multiplication
def multiply(a, b):
    return a * b

# IV. Division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Undefined (division by zero)"

# V. Modulo Division
def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Undefined (division by zero)"

# VI. Floor Division
def floor_division(a, b):
    if b != 0:
        return a // b
    else:
        return "Undefined (division by zero)"

#Asking for user input of the numbers for calculation
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# To print the result of the six respective arithmetic functions
print("\n--- Results ---")
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
print("Modulo Division:", modulo(num1, num2))
print("Floor Division:", floor_division(num1, num2))

# By Biplab Prasad Gajurel 25024641