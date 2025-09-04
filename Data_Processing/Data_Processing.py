# ******DATA PROCESSING USING SK LEARN******
# Q. Perform Data Preprocessing on melb_data.csv dataset with statistical perspective. The dataset can be downloaded from Kaggle Link

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

data = pd.read_csv("melb_data.csv")

print("***** ORIGINAL DATA *****")
print("Shape of dataset:", data.shape)
print("\nFirst 5 rows:\n", data.head())
print("\nMissing values (before cleaning):\n", data.isnull().sum())
print("\nStatistical Summary:\n", data.describe(include="all"))

data = data.fillna(data.median(numeric_only=True))   
data = data.fillna(data.mode().iloc[0])           

print("\nAFTER HANDLING MISSING VALUES ")
print("Missing values:\n", data.isnull().sum())

le = LabelEncoder()
for col in data.select_dtypes(include="object").columns:
    data[col] = le.fit_transform(data[col])

print("\n AFTER ENCODING CATEGORICAL DATA")
print(data.head())

X = data.drop("Price", axis=1) 
y = data["Price"]               

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\n FEATURES AFTER SCALING (first 5 rows) ")
print(X_scaled[:5])

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

print("\n===== TRAIN-TEST SPLIT =====")
print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)

# ******DATA PROCESSING USING PANDAS******
# Q. Perform Data Preprocessing on melb_data.csv dataset with statistical perspective. The dataset can be downloaded from Kaggle Link

import pandas as pd
data = pd.read_csv("melb_data.csv")

print(" ORIGINAL DATA ")
print("Shape of dataset:", data.shape)
print("\nFirst 5 rows:\n", data.head())
print("\nMissing values (before cleaning):\n", data.isnull().sum())
print("\nStatistical Summary:\n", data.describe(include="all"))

for col in data.select_dtypes(include="number").columns:
    data[col] = data[col].fillna(data[col].median())

for col in data.select_dtypes(include="object").columns:
    data[col] = data[col].fillna(data[col].mode()[0])

print("\n AFTER HANDLING MISSING VALUES ")
print("Missing values:\n", data.isnull().sum())

for col in data.select_dtypes(include="object").columns:
    data[col] = data[col].astype("category").cat.codes

print("\n AFTER ENCODING CATEGORICAL DATA ")
print(data.head())

print("\n CORRELATION MATRIX ")
print(data.corr())

print("\n FINAL DATA SHAPE ")
print(data.shape)
