'''The following program uses a numpy array and
does all the arithmetic calculations asked by the user and
displays the output of the calculations'''

import numpy as np

# Create a numpy array
arr = np.array([6, 7, 8, 9, 10])

# a) Sum of elements
total_sum = np.sum(arr)

# b) Average of elements
average = np.mean(arr)

# c) Maximum and Minimum values
max_value = np.max(arr)
min_value = np.min(arr)

# For displaying the results
print("Array:", arr)
print("Sum of elements:", total_sum)
print("Average of elements:", average)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

# by Biplab Prasad Gajurel 25024641