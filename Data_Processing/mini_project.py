# Q. Use-Case: House Price Prediction
# Dataset: melb_data.csv
# The dataset can be downloaded from Kaggle.
# Perform the following tasks:
# Load the data in dataframe (Pandas)
# Handle inappropriate data
# Handle the missing data

import pandas as pd
data = pd.read_csv("melb_data.csv")

print(" ORIGINAL DATA ")
print("Shape of dataset:", data.shape)
print("\nFirst 5 rows:\n", data.head())

data = data.drop_duplicates()

if "Price" in data.columns:
    data = data[data["Price"] > 0]

print("\n AFTER HANDLING INAPPROPRIATE DATA ")
print("Shape of dataset:", data.shape)

for col in data.select_dtypes(include="number").columns:
    data[col] = data[col].fillna(data[col].median())

for col in data.select_dtypes(include="object").columns:
    data[col] = data[col].fillna(data[col].mode()[0])

print("\n AFTER HANDLING MISSING DATA ")
print("Missing values:\n", data.isnull().sum().sum(), "missing values left")
s
for col in data.select_dtypes(include="object").columns:
    data[col] = data[col].astype("category").cat.codes

print("\n AFTER HANDLING CATEGORICAL DATA ")
print(data.head())

print("\nFinal dataset shape:", data.shape)
