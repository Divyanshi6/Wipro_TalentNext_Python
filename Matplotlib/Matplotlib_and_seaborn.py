# Perform Exploratory Data Analysis for the dataset Mall_Customers. The dataset can be downloaded from https://www.kaggle.com/datasets
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Mall_Customers.csv")

print("Shape:", data.shape)
print(data.head())
print(data.describe())

sns.countplot(x="Gender", data=data)
plt.title("Gender Distribution")
plt.show()

sns.histplot(data["Age"], bins=20, kde=True)
plt.title("Age Distribution")
plt.show()

sns.scatterplot(x="Annual Income (k$)", y="Spending Score (1-100)", hue="Gender", data=data)
plt.title("Income vs Spending Score")
plt.show()

sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Q. Perform Exploratory Data Analysis for the dataset salary_data. 
salary = pd.read_csv("salary_data.csv")

print("Shape:", salary.shape)
print(salary.head())
print(salary.describe())

sns.scatterplot(x="YearsExperience", y="Salary", data=salary)
plt.title("Years of Experience vs Salary")
plt.show()

sns.regplot(x="YearsExperience", y="Salary", data=salary, ci=None, color="red")
plt.title("Regression Line: Experience vs Salary")
plt.show()

# Q. Perform Exploratory Data Analysis for the dataset Social Network Ads

ads = pd.read_csv("Social_Network_Ads.csv")

print("Shape:", ads.shape)
print(ads.head())
print(ads.describe())

sns.histplot(ads["Age"], bins=20, kde=True)
plt.title("Age Distribution")
plt.show()

sns.countplot(x="Gender", hue="Purchased", data=ads)
plt.title("Purchase by Gender")
plt.show()

sns.scatterplot(x="Age", y="EstimatedSalary", hue="Purchased", data=ads)
plt.title("Age vs Salary (Purchased vs Not)")
plt.show()

sns.heatmap(ads.corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()
