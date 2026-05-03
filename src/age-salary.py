import os
import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = "data/Employee.csv"

if not os.path.exists(FILE_PATH):
    raise FileNotFoundError(f"CSV file not found: {FILE_PATH}")

# Load the data

df = pd.read_csv(FILE_PATH)
# Age vs Salary

x_column = "Age"
possible_y_columns = ["Salary", "ExperienceInCurrentDomain", "PaymentTier"]
selected_y_column = next((col for col in possible_y_columns if col in df.columns), None)

if x_column not in df.columns:
    print(f"Missing required column for visualization: {x_column}")
    print("Available columns:", ", ".join(df.columns))
elif selected_y_column is None:
    print("Missing required numeric target column for visualization.")
    print("Need one of:", ", ".join(possible_y_columns))
    print("Available columns:", ", ".join(df.columns))
else:
    plt.figure()
    plt.scatter(df[x_column], df[selected_y_column])
    plt.title(f"{x_column} vs {selected_y_column}")
    plt.xlabel(x_column)
    plt.ylabel(selected_y_column)
    plt.tight_layout()
    output_file = f"{x_column.lower()}_vs_{selected_y_column.lower()}.png"
    plt.savefig(output_file)
    plt.close()
    print(f"Graph saved as {output_file}")