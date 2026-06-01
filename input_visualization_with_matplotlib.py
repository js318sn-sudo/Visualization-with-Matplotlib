# Data Visualization with Matplotlib

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create Dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100, 120, 150, 180, 170, 200],
    "Profit": [20, 25, 30, 40, 35, 50]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Dataset
print("Dataset")
print(df)

# First 5 Rows
print("\nFirst 5 Rows")
print(df.head())

# Dataset Information
print("\nDataset Information")
df.info()

# Summary Statistics
print("\nSummary Statistics")
print(df.describe())

# Line Plot
plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("line_plot.png")
plt.show()

# Bar Plot
plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Sales"])
plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("bar_plot.png")
plt.show()

# Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Sales"], bins=5)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.savefig("scatter_plot.png")
plt.show()

# Insights
print("\nInsights")
print("1. Sales show an increasing trend from January to June.")
print("2. June recorded the highest sales value.")
print("3. Higher sales generally result in higher profit.")
print("4. The histogram shows the distribution of sales values.")
print("5. The scatter plot indicates a positive relationship between sales and profit.")


