import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = "data/Employee.csv"

# Load the data

df = pd.read_csv(FILE_PATH)

# Age Distribution histogram

if "Age" in df.columns:
    plt.figure()
    plt.hist(df["Age"])
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.savefig("age_distribution.png")
    plt.close()
    print("Graph saved as age_distribution.png")



# Age vs Salary

if "Age" in df.columns and "Salary" in df.columns:
    plt.figure()
    plt.scatter(df["Age"], df["Salary"])
    plt.title("Age Vs Salary")
    plt.xlabel("Age")
    plt.ylabel("Salary")
    plt.tight_layout()
    plt.savefig("salary_distribution.png")
    plt.close()
    print("Graph saved as salary_distribution.png")


