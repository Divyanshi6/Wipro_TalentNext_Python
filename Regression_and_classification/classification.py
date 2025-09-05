# Q1. Create a model that can predict the disease of cancer based on features given in the dataset. Use appropriate evaluation metrics.
# Dataset: cancer.csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("cancer.csv")
data = data.drop(["id", "Unnamed: 32"], axis=1)

X = data.drop("diagnosis", axis=1)
y = data["diagnosis"]

le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Cancer Prediction Results:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))


# Q2. Create a model that can predict that the customer has purchased item or not based on features given in the dataset. Use appropriate evaluation metrics.
# Dataset: Social_Network_Ads.csv
data = pd.read_csv("cancer.csv")
data = data.drop(["id", "Unnamed: 32"], axis=1)

X = data.drop("diagnosis", axis=1)
y = data["diagnosis"]

le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Cancer Prediction Results:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

