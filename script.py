#Import libraries
import pandas as pd
import matplotlib.pyplot as plt

#Exporting Data
df = pd.read_csv('lap.csv')

#Check Data Type
print(df.dtypes)

#Convert data types
df['Inches'] = pd.to_numeric(df['Inches'], errors='coerce')  
df['CPU_freq'] = pd.to_numeric(df['CPU_freq'], errors='coerce')

df['ScreenH'] = pd.to_numeric(df['ScreenH'], errors='coerce')
df['ScreenH'].fillna(0, inplace=True)
# Convert to integer
df['ScreenH'] = df['ScreenH'].astype(int)

#Recheck data types
print(df.dtypes)

#Check duplicates
Duplicates = df.duplicated()
print(Duplicates)

#Check *Null*
missing = df.isnull().sum
# Total missing values in the DataFrame
total_missing_values = df.isnull().sum().sum()
print(f'Total missing values: {total_missing_values}')

  Replace *Null*
# Define columns for which to use mean
mean_cols = ['Inches', 'CPU_freq']
# Replace missing values with the mean for these columns
df[mean_cols] = df[mean_cols].fillna(df[mean_cols].mean())

# Define columns for which to use median
median_cols = ['Price_euros']

# Replace missing values with the median for these columns
df[median_cols] = df[median_cols].fillna(df[median_cols].median())

# Define columns for which to use mode
mode_cols = ['RetinaDisplay']

# Replace missing values with mode for these columns
for col in mode_cols:
    mode_value = df[col].mode()[0]  # Get the most frequent value
    df[col] = df[col].fillna(mode_value)

df.fillna(0, inplace=True)

#Recheck missing *values*
if df.isnull().values.any():
    print("There are missing values in the dataset.")
else:
    print("No missing values in the dataset.")

