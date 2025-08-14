import pandas as pd
# Q1. Exercise 3: Pandas – DataFrame
# Download the dataset and rename to cars.csv
# Link (Dataset):
# https://www.kaggle.com/uciml/autompg-dataset/data?select=auto-mpg.csv
# or https://archive.ics.uci.edu/ml/datasets/Auto+MPG

# Tasks:
# a. Import Pandas
# b. Import the Cars Dataset and store the Pandas DataFrame in the variable cars
# c. Inspect the first 10 rows of the DataFrame cars
# d. Inspect the DataFrame cars by printing it
# e. Inspect the last 5 rows
# f. Get some meta information on our DataFrame

cars = pd.read_csv("cars.csv")  
print("\nFirst 10 Rows:\n", cars.head(10))
print("\nFull DataFrame:\n", cars)
print("\nLast 5 Rows:\n", cars.tail())
print("\nMeta Information:")
cars.info()


# Exercise 4: Download 50_startups dataset
# Link: https://www.kaggle.com/datasets/farhanmd29/50-startups
# Tasks:
# a. Create DataFrame using Pandas
# b. Read the data from 50_startups.csv file and load the data into a DataFrame
# c. Check the statistical summary
# d. Check for correlation coefficient between dependent and independent variables
    
startups = pd.read_csv("50_startups.csv")  
print("\nStatistical Summary:\n", startups.describe())

print("\nCorrelation Matrix:\n", startups.corr())
