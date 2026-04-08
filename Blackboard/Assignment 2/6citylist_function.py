'''The following program asks input of a list of cities and
asks input from the user for the city they want to search and
if it matches the list, returns index of city in stored list and
if not, returns a message'''

# Defining of a function to search for a city in the list and return its index
def search_city(cities, city_to_find):
    if city_to_find in cities:
        index = cities.index(city_to_find)
        return index
    else:
        return -1

# Asking the user to input the cities
print("Enter city names separated by spaces:")
user_input = input()
city_list = user_input.split()

# Asking the user for the city they want to search
print("Enter the city you want to search for:")
search_city_name = input()

# Calling the function
result = search_city(city_list, search_city_name)

# Showing output
if result != -1:
    print(search_city_name, "found at index", result)
else:
    print(search_city_name, "is not available in the list.")

# By Biplab Prasad Gajurel 25024641