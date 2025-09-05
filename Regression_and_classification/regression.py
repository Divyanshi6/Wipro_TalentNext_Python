# Q1. Predict the price of the car based on its features.
# Use appropriate evaluation metrics. Dataset: cars.csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = pd.read_csv(r"C:\Users\sdivy\WiproTalentnext\cars.csv")
data = data.drop("car name", axis=1)
data = data.apply(pd.to_numeric, errors='coerce')
data = data.fillna(data.mean())
X = data.drop("mpg", axis=1)
y = data["mpg"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))


# Q2. Create a model that can predict the profit based on its features.
# Use appropriate evaluation metrics. Dataset: 50_startups.csv (from Kaggle)
data = pd.read_csv(r"C:\Users\sdivy\WiproTalentnext\50_startups.csv")
data = pd.get_dummies(data, drop_first=True)

X = data.drop("Profit", axis=1)
y = data["Profit"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Startup Profit Prediction")
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Q3. Create a model that can predict the salary based on experience.
# Use appropriate evaluation metrics. Dataset: Salary_Data.csv
salary = pd.read_csv(r"C:\Users\sdivy\WiproTalentnext\Salary_Data.csv")
print("Columns in Salary_Data:", salary.columns)

if "YearsExperience" in salary.columns:
    salary.rename(columns={"YearsExperience": "Years of Experience"}, inplace=True)

salary = salary.dropna()

X = salary[["Years of Experience"]]  
y = salary["Salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Salary Prediction")
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
