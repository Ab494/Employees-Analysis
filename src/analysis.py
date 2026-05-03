import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
FILE_PATH = "data/Employee.csv"

df = pd.read_csv(FILE_PATH)

# 1 Show first 5 rows of the dataset
print("=== FIRST 5 ROWS===")
print(df.head(20))


# 2 Show columns names
print("\n=== COLUMNS ===")
print(df.columns)

# 3 Total number of records
print("\n=== TOTAL RECORDS ===")
print(len(df))

# AGE ANALYSIS

if "Age" in df.columns:
    print("\n=== Age Analysis ===")
    print("Average Age:", np.mean(df["Age"]))
    print("Youngest Age:", np.min(df["Age"]))
    print("Oldest Age:", np.max(df["Age"]))

# FILTERING 

# Employees older than 30
if "Age" in df.columns:
    print("n\=== Employees Above 30 ===")
    above_30 = df[df["Age"] > 30]
    print(above_30)

    
