import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("titanic.csv")

# Plot 1: Survival Count
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()

# Plot 2: Survival by Gender
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title("Survival by Gender")
plt.show()
