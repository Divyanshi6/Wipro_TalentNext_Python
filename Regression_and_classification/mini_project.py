# Q1. Use Case: Sales Prediction
# Create a model which will predict the sales based on campaigning expenses.
# Dataset: Advertising.csv
# (The dataset can be downloaded from Kaggle)
# Perform the following tasks:
# Load the data in the DataFrame.
# Perform Data Preprocessing.
# Handle Categorical Data.
# Perform Exploratory Data Analysis (EDA).
# Build the model using Multiple Linear Regression.
# Use the appropriate evaluation metrics.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("Advertising.csv")
print(data.head())

if "Unnamed: 0" in data.columns:
    data = data.drop("Unnamed: 0", axis=1)

sns.pairplot(data, x_vars=["TV", "Radio", "Newspaper"], y_vars="Sales", height=4, aspect=1, kind="scatter")
plt.show()

corr = data.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

X = data[["TV", "Radio", "Newspaper"]]
y = data["Sales"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Sales Prediction Results:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
results = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
print(results.head())



# Q2. Use Case: Diabetes Prediction
# Consider the PIMA Indians diabetes dataset. Create a model for diabetes prediction based on the features mentioned in the dataset.
# Dataset: PIMA Indians diabetes dataset (available on Kaggle)
# Perform the following tasks:
# Load the data in the DataFrame.
# Perform Data Preprocessing.
# Perform Exploratory Data Analysis.
# Build the model using Logistic Regression and K-Nearest Neighbour.
# Use the appropriate evaluation metrics
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv("diabetes.csv")   

X = data.drop("Outcome", axis=1)
y = data["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
y_pred_log = log_model.predict(X_test)

print("Logistic Regression Results")
print("Accuracy:", accuracy_score(y_test, y_pred_log))
print(classification_report(y_test, y_pred_log))

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
y_pred_knn = knn_model.predict(X_test)

print("\nKNN Results")
print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print(classification_report(y_test, y_pred_knn))
