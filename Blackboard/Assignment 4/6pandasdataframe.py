'''The following program reads data from the csv file, adds
two extra factors of BMI and Risk and
displays the output by corresponding to each preset health conditions'''

import pandas as pd

# To read the CSV
try:
    df = pd.read_csv("weight_height.csv")
    print("\nLoaded data:")
    print(df)
except FileNotFoundError:
    print("Error: File not found.")
    exit()

# Calculation of BMI (standard formula)
df['Height_m'] = df['Height'] / 100
df['BMI'] = df['Weight'] / (df['Height_m'] ** 2)

# Defining risk classification function
def classify_risk(bmi):
    if bmi < 18.5:
        return "Nutrient deficient"
    elif 18.5 <= bmi <= 24.9:
        return "lower risk"
    elif 25 <= bmi <= 29.9:
        return "Heart disease risk"
    elif 30 <= bmi <= 34.9:
        return "Higher risk of diabetes, heart disease"
    elif bmi >= 40:
        return "Serious health condition risk"
    else:
        return "Unknown"

# Application of classification
df['Risk'] = df['BMI'].apply(classify_risk)

# To show the updated DataFrame
print("\nData with BMI and Risk:")
print(df)

# To optionally save to new CSV
df.to_csv("weight_height_updated.csv", index=False)
print("\nUpdated file saved as 'weight_height_updated.csv'.")

# by Biplab Prasad Gajurel 25024641