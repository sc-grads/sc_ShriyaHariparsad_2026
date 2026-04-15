import pandas as pd
import logging

#configure logging
logging.basicConfig(filename='../output/log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Load data
df = pd.read_csv('../data/Messy_Sales_Data.csv')
logging.info("Python Messy_Sales_Data.csv loaded successfully")

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Define region and salesperson relationship
region_map = {
    'North': 'John',
    'South': 'Mary',
    'East': 'David',
    'West': 'Sarah'
}

# Fill missing names based on region
df['salesperson'] = df['salesperson'].fillna(df['region'].map(region_map))

# Calculate mean per category and round it up to nearest whole number
df['quantity'] = df.groupby('category')['quantity'].transform(lambda x: x.fillna(int(x.mean() + 0.9999))).astype(int)
logging.info("Filled missing quantity values with rounded off averages")

# Remove duplicates
df = df.drop_duplicates()

# Convert date column
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Save cleaned data
df.to_csv('../output/clean_sales.csv', index=False)

print(df.head())
print(df.columns)
print(df.info())

print("Data cleaned successfully")

# DATA TRANSFORMATION

# Create revenue column
df['revenue'] = df['quantity'] * df['price']
logging.info("Revenue column created")