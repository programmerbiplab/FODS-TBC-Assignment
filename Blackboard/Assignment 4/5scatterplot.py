'''The following program reads data from the csv file and
displays meaningful output of data in the form of scatterplot'''

import pandas as pd
import matplotlib.pyplot as plt

# To read the CSV file
try:
    data = pd.read_csv("weight_height.csv")
    print("CSV file loaded successfully.")
except FileNotFoundError:
    print("Error: 'weight_height.csv' file not found.")
    exit()
except Exception as e:
    print("An error occurred while reading the CSV file:", e)
    exit()

# Displaying the first few rows to verify
print("\nSample data:")
print(data.head())

# For the creation of scatterplots

# a) Weight vs Height
plt.figure(figsize=(6, 4))
plt.scatter(data['Weight'], data['Height'], color='blue')
plt.title('Weight vs Height')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.grid(True)
plt.show()

# b) Age vs Weight
plt.figure(figsize=(6, 4))
plt.scatter(data['Age'], data['Weight'], color='green')
plt.title('Age vs Weight')
plt.xlabel('Age')
plt.ylabel('Weight')
plt.grid(True)
plt.show()

# c) Height vs Age
plt.figure(figsize=(6, 4))
plt.scatter(data['Height'], data['Age'], color='red')
plt.title('Height vs Age')
plt.xlabel('Height')
plt.ylabel('Age')
plt.grid(True)
plt.show()

# d) Gender vs Height
plt.figure(figsize=(6, 4))
plt.scatter(data['Gender'], data['Height'], color='purple')
plt.title('Gender vs Height')
plt.xlabel('Gender')
plt.ylabel('Height')
plt.grid(True)
plt.show()

# e) Gender vs Weight
plt.figure(figsize=(6, 4))
plt.scatter(data['Gender'], data['Weight'], color='orange')
plt.title('Gender vs Weight')
plt.xlabel('Gender')
plt.ylabel('Weight')
plt.grid(True)
plt.show()

# by Biplab Prasad Gajurel 25024641