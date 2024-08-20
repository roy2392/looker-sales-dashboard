import pandas as pd

# Load the cleaned data
file_path = 'data/processed_sales_data_cleaned.csv'
df_cleaned = pd.read_csv(file_path)

# Create Date Dimension
df_cleaned['Order Date'] = pd.to_datetime(df_cleaned['Order Date'])
date_dim = df_cleaned[['Order Date']].drop_duplicates().reset_index(drop=True)
date_dim['Date Key'] = date_dim.index + 1
date_dim['Year'] = date_dim['Order Date'].dt.year
date_dim['Quarter'] = date_dim['Order Date'].dt.quarter
date_dim['Month'] = date_dim['Order Date'].dt.month
date_dim['Day'] = date_dim['Order Date'].dt.day

# Create Product Dimension
product_dim = df_cleaned[['Item Type']].drop_duplicates().reset_index(drop=True)
product_dim['Product Key'] = product_dim.index + 1

# Create Region Dimension
region_dim = df_cleaned[['Region', 'Country']].drop_duplicates().reset_index(drop=True)
region_dim['Region Key'] = region_dim.index + 1

# Save dimension tables
date_dim.to_csv('data/dim_date.csv', index=False)
product_dim.to_csv('data/dim_product.csv', index=False)
region_dim.to_csv('data/dim_region.csv', index=False)

print("Dimension tables saved.")

# Map Date Key to Fact Table
df_fact = df_cleaned.merge(date_dim, on='Order Date', how='left')

# Map Product Key to Fact Table
df_fact = df_fact.merge(product_dim, on='Item Type', how='left')

# Map Region Key to Fact Table
df_fact = df_fact.merge(region_dim, on=['Region', 'Country'], how='left')

# Select and reorder columns for the Fact Table
fact_table = df_fact[['Date Key', 'Product Key', 'Region Key', 'Units Sold', 
                      'Total Revenue', 'Total Cost', 'Total Profit']]

# Save the Fact Table
fact_table.to_csv('data/fact_sales.csv', index=False)

print("Fact table saved.")