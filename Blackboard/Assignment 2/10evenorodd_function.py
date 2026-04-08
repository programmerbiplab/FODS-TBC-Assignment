'''The following program takes continuous input of numbers from the user and
classifies the input numbers into odd and even list and
once the user is done with input, the program displays all the numbers in proper format'''

# Initializing empty lists for even and odd numbers at the start of program
even_numbers = []
odd_numbers = []

# Output screen initial message
print("Enter numbers one by one. Type 'exit' to stop.")

while True:
    user_input = input("Enter a number (or 'exit' to stop): ")
    
    if user_input.lower() == 'exit':
        break

    # Try to convert input to integer
    try:
        number = int(user_input)
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    except ValueError:
        print("Invalid input! Please enter a number or 'exit'.")

# Displaying the results
print("\n--- Result ---")
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

# By Biplab Prasad Gajurel 25024641
