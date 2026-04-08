'''The following takes input of numbers from user and
sorts them and performs slicing operations to get elements
defined by indexes'''

# Taking at least 10 numbers from the user
numbers = []

print("Enter at least 10 numbers:")

while len(numbers) < 10:
    try:
        num = int(input(f"Enter number {len(numbers) + 1}: "))
        numbers.append(num)
    except ValueError:
        print("Please enter a valid integer.")

# Sorting the list
numbers.sort()

print("\nSorted list:", numbers)

# Slicing operations as requested in question
slice_2_5 = numbers[2:6]  # indexes 2 to 5 inclusive, so end is 6
slice_5_8 = numbers[5:9]  # indexes 5 to 8 inclusive, so end is 9
slice_2_9 = numbers[2:10] # indexes 2 to 9 inclusive, so end is 10

print("Elements from index 2 to 5:", slice_2_5)
print("Elements from index 5 to 8:", slice_5_8)
print("Elements from index 2 to 9:", slice_2_9)

# by Biplab Prasad Gajurel 25024641