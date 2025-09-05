# Use Case: Diabetes Prediction
# Perform Exploratory Data Analysis for the Diabetes Dataset.
# Dataset: Diabetes.csv
# The dataset can be downloaded from Kaggle
# Tasks to Perform:
# Load the data in the DataFrame
# Data Pre-processing
# Handle the Categorical Data
# Perform Uni-variate Analysis
# Perform Bi-variate Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Diabetes.csv")
print(" Dataset Information ")
print(data.shape)
print(data.head())
print(data.info())
print(data.describe())

print("\nMissing values:\n", data.isnull().sum())
cols_with_zero = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
data[cols_with_zero] = data[cols_with_zero].replace(0, np.nan)

print("\nMissing values after replacing 0s:\n", data.isnull().sum())
data.fillna(data.median(numeric_only=True), inplace=True)

print("\nValue counts for Outcome (target variable):")
print(data["Outcome"].value_counts())

sns.countplot(x="Outcome", data=data)
plt.title("Diabetes Outcome Distribution")
plt.show()

data.hist(bins=20, figsize=(12, 10))
plt.suptitle("Histogram of Features", size=16)
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(data=data)
plt.title("Boxplot of All Features")
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

sns.pairplot(data[["Glucose", "BMI", "Age", "Outcome"]], hue="Outcome")
plt.show()
