import pandas as pd

# Load datasets from CSV and JSON files
csv_data = pd.read_csv('csv_data.csv')
json_data = pd.read_json('json_data.json')

# Display the first 10 rows and the last 10 rows of each dataset
print("CSV Data:")
print("First 10 rows:")
print(csv_data.head(10))
print("Last 10 rows:")
print(csv_data.tail(10))

print("\nJSON Data:")
print("First 10 rows:")
print(json_data.head(10))
print("Last 10 rows:")
print(json_data.tail(10))

# Display the unique values and the number of unique values in a specific column of each dataset
print("\nCSV Data:")
print("Unique values in 'column_name' column:")
print(csv_data['column_name'].unique())
print("Number of unique values in 'column_name' column:")
print(csv_data['column_name'].nunique())

print("\nJSON Data:")
print("Unique values in 'column_name' column:")
print(json_data['column_name'].unique())
print("Number of unique values in 'column_name' column:")
print(json_data['column_name'].nunique())

# Generate descriptive statistics for each dataset
print("\nCSV Data Descriptive Statistics:")
print(csv_data.describe())

print("\nJSON Data Descriptive Statistics:")
print(json_data.describe())

# Display concise summaries of each dataset
print("\nCSV Data Info:")
print(csv_data.info())

print("\nJSON Data Info:")
print(json_data.info())

# Identify the columns with missing data in each dataset
print("\nCSV Data Columns with Missing Values:")
print(csv_data.columns[csv_data.isnull().any()])

print("\nJSON Data Columns with Missing Values:")
print(json_data.columns[json_data.isnull().any()])

# Fill missing values in a numerical column with the mean, mode, and median
csv_data['numerical_column'].fillna(csv_data['numerical_column'].mean(), inplace=True)
json_data['numerical_column'].fillna(json_data['numerical_column'].mean(), inplace=True)

csv_data['numerical_column'].fillna(csv_data['numerical_column'].mode()[0], inplace=True)
json_data['numerical_column'].fillna(json_data['numerical_column'].mode()[0], inplace=True)

csv_data['numerical_column'].fillna(csv_data['numerical_column'].median(), inplace=True)
json_data['numerical_column'].fillna(json_data['numerical_column'].median(), inplace=True)

# Fill missing values in a categorical column with the mode
csv_data['categorical_column'].fillna(csv_data['categorical_column'].mode()[0], inplace=True)
json_data['categorical_column'].fillna(json_data['categorical_column'].mode()[0], inplace=True)

# Drop rows and columns with missing values from each dataset
csv_data.dropna(inplace=True)
json_data.dropna(inplace=True)

csv_data.dropna(axis=1, inplace=True)
json_data.dropna(axis=1, inplace=True)

# Create a new column in each dataset based on existing columns
csv_data['new_column'] = csv_data['column1'] + csv_data['column2']
json_data['new_column'] = json_data['column1'] + json_data['column2']

# Drop a specific column from each dataset
csv_data.drop('column_to_drop', axis=1, inplace=True)
json_data.drop('column_to_drop', axis=1, inplace=True)

# Drop a specific row from each dataset
csv_data.drop(csv_data.index[0], inplace=True)
json_data.drop(json_data.index[0], inplace=True)

# Separate the features (X) and the target variable (y) in one of the datasets
X = csv_data.drop('target_variable', axis=1)
y = csv_data['target_variable']

print("\nFirst 5 rows of X:")
print(X.head(5))

print("\nFirst 5 rows of y:")
print(y.head(5))