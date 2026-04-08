'''The following program takes user input of a list of numbers and
displays output by removing any duplicate number from the provided list of
numbers by the user'''

# Function to remove duplicates from a list
def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

# Asking the user for input
print("Enter numbers separated by spaces:")
user_input = input()

# Converting input into a list of integers
number_list = [int(num) for num in user_input.split()]

# Calling of the function
result = remove_duplicates(number_list)

# Print the list of numbers without duplicates
print("List without duplicates:")
print(result)

# By Biplab Prasad Gajurel 25024641