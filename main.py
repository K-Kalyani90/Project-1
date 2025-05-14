import pandas as pd

dataset = pd.read_csv('Walmart.csv')

print(dataset.describe())

columns = ["Weekly_Sales", "Holiday_Flag", "Temperature", "Fuel_Price", "CPI", "Unemployment"]

for column in columns:
    print(f"Mean: {dataset[column].mean()}")
    print(f"Median: {dataset[column].median()}")
    print(f"Mode: {dataset[column].mode()}")

import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(a)

print("Mean: ", np.mean(a))
print("Median: ", np.median(a))
print("Standard Deviation: ", np.std(a))
print("Variance: ", np.var(a))
print("Sum: ", np.sum(a))
print("Product: ", np.prod(a))
print("Max: ", np.max(a))
print("Min: ", np.min(a))

data = {
    "Name": ["John", "Jane", "Jim", "Jill"],
    "Age": [20, 30, 40, 50]
}

df = pd.DataFrame(data)

print(df)

print("Average Age: ", df["Age"].mean())
print("Median Age: ", df["Age"].median())
print("Standard Deviation of Age: ", df["Age"].std())
print("Variance of Age: ", df["Age"].var())

from scipy import stats

#Generate a random sample from a normal distribution
#sample = np.random.normal(loc=0, scale=1, size=1000)

#print("Mean: ", sample)

#Data Visualization

import matplotlib.pyplot as plt

data1 = { 
   "Student": ["Alice", "Bob", "Charlie", "David", "Eve"],
   "Math": [85, 96, 75, 86, 85],
   "Science": [99, 87, 88, 92, 93],
   "English": [89, 95, 78, 83, 90],
   "Gender": ["Female", "Male", "Female", "Male", "Male"] 
}

df2 = pd.DataFrame(data1)

print(df2)

plt.figure(figsize=(10, 6))
plt.plot(df2["Student"], df2["Math"], color="blue", label="Math")
plt.plot(df2["Student"], df2["Science"], color="green", label="Science")
plt.plot(df2["Student"], df2["English"], color="red", label="English")
plt.legend()
plt.show()