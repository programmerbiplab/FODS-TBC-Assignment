'''The following program with function counts and prints occurences of all the numbers from the list and
prints the total number of times the input number is repeated and
displays the repitition number as output'''

# Defining a function to count and print occurrences of each number in the provided list
def count_occurrences(numbers):
    occurrences = {}
    for num in numbers:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1

    print("Number occurrences:")
    for num, count in occurrences.items():
        print(num, "occurs", count, "times")
    print() 

# Ask the user for their input
print("Enter numbers separated by spaces:")
user_input = input()

# Convert the input string to a list of integers
number_list = user_input.split()
number_list = [int(num) for num in number_list]

# Calling the function
print("User Test:")
count_occurrences(number_list)

# By Biplab Prasad Gajurel 25024641
