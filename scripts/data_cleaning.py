import os
import pandas as pd

# Define the file paths
input_file_path = 'data/raw_sales_data.csv'
output_file_path = 'data/processed_sales_data_cleaned.csv'

# Ensure the 'data' directory exists
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# Load the raw data
df = pd.read_csv(input_file_path)

# 1. Handle Missing Values
df_cleaned = df.dropna()

# 2. Remove Duplicates
df_cleaned = df_cleaned.drop_duplicates()

# 3. Correct Data Types
df_cleaned['Order Date'] = pd.to_datetime(df_cleaned['Order Date'])
numeric_columns = ['Units Sold', 'Unit Price', 'Unit Cost', 'Total Revenue', 'Total Cost', 'Total Profit']
df_cleaned[numeric_columns] = df_cleaned[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Recheck for any remaining NaNs after type conversion
df_cleaned = df_cleaned.dropna()

# 4. Standardize Data (Optional)
# df_cleaned['Country'] = df_cleaned['Country'].str.strip().str.title()

# 5. Outlier Detection
mean_profit = df_cleaned['Total Profit'].mean()
std_profit = df_cleaned['Total Profit'].std()
outlier_threshold = 3 * std_profit
df_cleaned = df_cleaned[(df_cleaned['Total Profit'] >= (mean_profit - outlier_threshold)) & 
                        (df_cleaned['Total Profit'] <= (mean_profit + outlier_threshold))]

# Save the cleaned data to a new CSV file
df_cleaned.to_csv(output_file_path, index=False)

print(f"Cleaned and processed data saved to {output_file_path}")