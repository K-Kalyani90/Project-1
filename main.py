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


sample = np.random.normal(loc=0, scale=1, size=1000)

print("Mean: ", sample)