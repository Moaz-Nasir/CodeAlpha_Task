import pandas as pd

# Load the dataset
df = pd.read_csv("titanic.csv")

# Display first 5 rows
print("Head of dataset:\n", df.head())

# Show dataset info
print("\nData Types and Non-Null Values:")
print(df.info())

# Show summary statistics
print("\nStatistical Summary:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
