'''The following program creates a function and
inputs two numbers and performs mathematical calculations based
on user requests'''

# creation of a function with two parameters for two numbers
def calculate_operations(a, b):
    print("Sum:", a + b)
    print("Difference (a-b):", a - b)
    print("Difference (b-a):", b - a)
    print("Product:", a * b)
    print("Remainder (a % b):", a % b)
    print("Remainder (b % a):", b % a)

# To ask the input of two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# To print the calculations
calculate_operations(num1, num2)

# By Biplab Prasad Gajurel 25024641