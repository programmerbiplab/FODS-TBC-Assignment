'''The following program takes input of two matrixes, validates them and
performs arithmetic calculations based on the user input of two matrixes'''

import numpy as np

# Defining the function
def input_matrix(rows, cols, name):
    print(f"\nEnter elements for {name} matrix:")
    elements = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(val)
        elements.append(row)
    return np.array(elements)

try:
    # Geting dimensions from the user for matrixes
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    # Getting input of two matrices
    matrix1 = input_matrix(rows, cols, "first")
    matrix2 = input_matrix(rows, cols, "second")

    print("\nFirst Matrix:\n", matrix1)
    print("\nSecond Matrix:\n", matrix2)

    # Matrix Addition
    try:
        addition = np.add(matrix1, matrix2)
        print("\nAddition Result:\n", addition)
    except ValueError:
        print("\nError: Matrices must be of same dimensions for addition.")

    # Matrix Subtraction
    try:
        subtraction = np.subtract(matrix1, matrix2)
        print("\nSubtraction Result:\n", subtraction)
    except ValueError:
        print("\nError: Matrices must be of same dimensions for subtraction.")

    # Matrix Multiplication
    try:
        if matrix1.shape[1] != matrix2.shape[0]:
            raise ValueError("Matrix multiplication not possible. Columns of first must equal rows of second.")
        multiplication = np.dot(matrix1, matrix2)
        print("\nMultiplication Result:\n", multiplication)
    except ValueError as e:
        print("\nError:", e)

# Validation if the calculation was correct
except Exception as e:
    print("\nAn error occurred:", e)

# by Biplab Prasad Gajurel 25024641
