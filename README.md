# Employee Project

This project contains simple employee dataset analysis and visualization scripts built with Python, Pandas, NumPy, and Matplotlib.

## Project Structure

- `data/Employee.csv` - Employee dataset CSV.
- `src/analysis.py` - Basic dataset exploration and age statistics.
- `src/visualize.py` - Generates an age distribution histogram and, if available, age vs salary scatter plot.
- `src/age-salary.py` - Generates a scatter plot of employee `Age` against a numeric target column.
- `env/` - Python virtual environment used for project dependencies.

## Dataset Overview

The current dataset includes columns such as:

- `Education`
- `JoiningYear`
- `City`
- `PaymentTier`
- `Age`
- `Gender`
- `EverBenched`
- `ExperienceInCurrentDomain`
- `LeaveOrNot`

> Note: The dataset does not always contain a `Salary` column, so `src/age-salary.py` falls back to `ExperienceInCurrentDomain` or `PaymentTier` automatically.

## Setup

If you already have the virtual environment in `env/`, use it directly:

```bash
cd /home/vanso/Downloads/Employee-project
./env/bin/python --version
```

If you need to recreate the environment:

```bash
python3 -m venv env
source env/bin/activate
pip install pandas numpy matplotlib
```

## Usage

### 1. Run dataset analysis

```bash
./env/bin/python src/analysis.py
```

This prints:

- first rows of the dataset
- column names
- total number of records
- average, minimum, and maximum age
- a filtered table of employees older than 30

### 2. Generate visualizations

```bash
./env/bin/python src/visualize.py
```

This saves:

- `age_distribution.png`
- `salary_distribution.png` (only if `Salary` exists in the dataset)

### 3. Generate age-based scatter plot

```bash
./env/bin/python src/age-salary.py
```

This saves a scatter plot file named automatically from the selected columns, for example:

- `age_vs_experienceincurrentdomain.png`

## Notes

- `src/visualize.py` was updated to save plots directly using `plt.savefig()` and avoid `plt.show()` in a headless environment.
- `src/age-salary.py` now checks for the CSV file and prints a clear message if required columns are missing.

## Troubleshooting

- If you see a message that `Salary` is missing, use `src/age-salary.py`, which automatically selects an available numeric column.
- If you are on a machine without a display, the scripts save charts to PNG files instead of opening interactive windows.
