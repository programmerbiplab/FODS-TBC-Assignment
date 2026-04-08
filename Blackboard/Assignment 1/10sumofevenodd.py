'''The following program is a menu driven program that asks user input of numbers and
calculates the sum of even and odd numbers continuosly until
the user exits from the program and display the sum at the end'''

#The starting of the sum variable is zero since the values keep on adding continuosly as per user demand
even_sum = 0
odd_sum = 0

while True:
    #To ask user input for every number
    user_input = input("Enter a number: ")

    if user_input.isdigit():
        num = int(user_input)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    else:
        print("Invalid input! Please enter a valid number.")
        continue

    # Ask if user wants to continue adding the numbers
    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice != 'yes':
        break
#To display the output of the sum stored in their respective odd or even variables
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

#by Biplab Prasad Gajurel 25024641