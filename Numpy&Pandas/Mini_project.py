# MINI PROJECT
# Use Case: Perform the Outlier detection for the given dataset i.e. datasetExample
# Dataset: datasetExample.csv
# Perform the following task
# Load the data in the DataFrame.
# Detection of Outliers.
df = pd.read_csv("datasetExample.csv") 
print("First 5 rows of the dataset:")
print(df.head())

def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

for col in numeric_cols:
    outliers = detect_outliers_iqr(df, col)
    print(f"\nOutliers in '{col}':")
    print(outliers if not outliers.empty else "No outliers found")
