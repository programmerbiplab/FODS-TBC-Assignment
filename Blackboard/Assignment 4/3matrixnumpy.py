'''The following program takes random array integer input from the user and
sorts them and does the matrix reshaping arithmetic process and displays the output '''

import numpy as np

# Creation of 1D numpy array of 10 random integers between 1 and 100
arr = np.random.randint(1, 101, size=10)
print("Original array:", arr)

# Sorting the array
sorted_arr = np.sort(arr)
print("Sorted array:", sorted_arr)

# First 2 rows and 5 columns matrix
try:
    reshaped_2_5 = sorted_arr.reshape(2, 5)
    print("\nReshaped to 2 x 5 matrix:\n", reshaped_2_5)
except ValueError:
    print("Cannot reshape to 2 x 5 matrix")

# Second, 5 rows and 2 columns matrix
try:
    reshaped_5_2 = sorted_arr.reshape(5, 2)
    print("\nReshaped to 5 x 2 matrix:\n", reshaped_5_2)
except ValueError:
    print("Cannot reshape to 5 x 2 matrix")

# by Biplab Prasad Gajurel 25024641