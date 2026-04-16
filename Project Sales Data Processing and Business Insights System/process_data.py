import pandas as pd
import logging

#configure logging
logging.basicConfig(filename='../output/log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Load data
df = pd.read_csv('../data/Messy_Sales_Data.csv')
logging.info("Python Messy_Sales_Data.csv loaded successfully")

# Standardise column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
logging.info("Column names standardised, removed spaces and converted to lowercase, replaced spaces with underscores")

# Define region and salesperson relationship
region_map = {
    'North': 'John',
    'South': 'Mary',
    'East': 'David',
    'West': 'Sarah'
}
logging.info("Region and salesperson defined clearly")

# Fill missing names based on region
df['salesperson'] = df['salesperson'].fillna(df['region'].map(region_map))
logging.info("Based on region, missing salesperson names filled successfully")

# Calculate mean per category and round it up to nearest whole number
df['quantity'] = df.groupby('category')['quantity'].transform(lambda x: x.fillna(int(x.mean() + 0.9999))).astype(int)
logging.info("Filled missing quantity values with rounded off averages")

# Remove duplicates
df = df.drop_duplicates()
logging.info("Duplicate rows removed successfully")

# Convert to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')
logging.info("Converts the date column from a string to a datetime format")

print(df.to_string())
print(df.columns)
print(df.info())
print("Data cleaned successfully")


# Create Revenue column
df['revenue'] = df['quantity'] * df['price']
logging.info("Revenue column created successfully")

# Month extracted from date
df['month'] = df['date'].dt.strftime('%B')
logging.info("Month column extracted from date successfully using the full month name")
print(df.to_string())

# Save cleaned data
df.to_csv('../output/clean_sales.csv', index=False)
logging.info("Cleaned data saved successfully")

# Aggregations
sales_by_region = df.groupby('region')['revenue'].sum().reset_index()
logging.info("Sales by region calculated successfully")
sales_by_product = df.groupby('product')['revenue'].sum().reset_index()
logging.info("Sales by product calculated successfully")
monthly_revenue = df.groupby('month')['revenue'].sum().reset_index()
logging.info("Monthly revenue calculated successfully")
salesperson_performance = df.groupby('salesperson')['revenue'].sum().reset_index()
logging.info("Salesperson performance calculated successfully")

# Save outputs
sales_by_region.to_csv('../output/sales_by_region.csv', index=False)
sales_by_product.to_csv('../output/sales_by_product.csv', index=False)
monthly_revenue.to_csv('../output/monthly_revenue.csv', index=False)
salesperson_performance.to_csv('../output/salesperson_performance.csv', index=False)

logging.info("All aggregated files saved")
print("revenue and month columns added successfully")
