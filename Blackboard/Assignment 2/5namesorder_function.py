'''The following program asks user input of names and
displays the names in a sepcific alphabetical order'''

# Defining a function to accept a list of names and return them in sorted order
def sort_names(names):
    sorted_list = sorted(names)
    return sorted_list

# Asking the user to enter names separated by spaces
print("Enter names separated by spaces:")
user_input = input()

# Converting input string to list of names
name_list = user_input.split()

# Calling the function
sorted_names = sort_names(name_list)

# Print the input names in a sorted format
print("Sorted names:")
for name in sorted_names:
    print(name)

# By Biplab Prasad Gajurel 25024641