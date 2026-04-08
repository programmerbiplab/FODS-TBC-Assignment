'''The following program takes user input and
does the mathematical calculations given below and
displays the output as long as the user wants to keep
giving a number input and once the user exits, the program ends with a message'''

# In order to extract date and time from system
import datetime

# Creating a file to store/execute the given question
filename = "math_results.txt"

# Defining a function for arithmetic calculations
def perform_operations(numbers):
    addition = sum(numbers)
    
    subtraction = numbers[0]
    for num in numbers[1:]:
        subtraction -= num

    multiplication = 1
    for num in numbers:
        multiplication *= num

    division = numbers[0]
    for num in numbers[1:]:
        if num != 0:
            division /= num
        else:
            division = "Error (division by zero)"
            break

    return addition, subtraction, multiplication, division

# Defining another function to work on the file that stores the data
def write_to_file(numbers, results):
    now = datetime.datetime.now()
    with open(filename, "a") as file:
        file.write("=====================================\n")
        file.write(f"Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Input Numbers     : {numbers}\n")
        file.write(f"Addition          : {results[0]}\n")
        file.write(f"Subtraction       : {results[1]}\n")
        file.write(f"Multiplication    : {results[2]}\n")
        file.write(f"Division          : {results[3]}\n")
        file.write("=====================================\n\n")


def read_file():
    print("\n=====================================")
    print("      Summary of All Operations")
    print("=====================================\n")
    with open(filename, "r") as file:
        content = file.read()
        print(content)


# Main Program Loop
while True:
    print("\nEnter a list of numbers (space-separated):")
    try:
        user_input = input(">> ")
        number_list = [float(num) for num in user_input.split()]
        if len(number_list) < 2:
            print("Please enter at least two numbers.")
            continue
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    results = perform_operations(number_list)
    write_to_file(number_list, results)

    choice = input("Do you want to perform another operation? (yes/no): ").strip().lower()
    if choice != "yes":
        break

# To show the summary
read_file()

# by Biplab Prasad Gajurel 25024641