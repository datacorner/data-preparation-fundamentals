import pandas as pd

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

def create_dimension_tables(df):
    """Create dimension tables
    Args:
        df (dataframe): dataset
    Returns:
        dataframe[]: list of dimension tables as dataframe
    """
    customer_dim = df[['Customer Name', 
                        'Segment', 'State']].drop_duplicates()
    customer_dim['Customer_Key'] = range(1, len(customer_dim) + 1)
    product_dim = df[['Product Name', 
                        'Category', 'Sub-Category']].drop_duplicates()
    product_dim['Product_Key'] = range(1, len(product_dim) + 1)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    date_dim = pd.DataFrame({
        'Date': pd.date_range(start=df['Order Date'].min(), 
                                end=df['Order Date'].max()),
    })
    date_dim['Year'] = date_dim['Date'].dt.year
    date_dim['Month'] = date_dim['Date'].dt.month
    date_dim['Quarter'] = date_dim['Date'].dt.quarter
    date_dim['Date_Key'] = range(1, len(date_dim) + 1)
    return customer_dim, product_dim, date_dim

def create_fact_table(df, customer_dim, product_dim, date_dim):
    """Create Fact table
    Args:
        df (dataframe): dataset
    Returns:
        dataframe: Fact table
    """
    # Merge Customer Dimension Key
    fact_table = df.merge(customer_dim, on=['Customer Name', 'Segment', 'State'], how='left')
    # Merge Product Dimension Key
    fact_table = fact_table.merge(product_dim, on=['Product Name', 'Category', 'Sub-Category'], how='left')
    # Merge Date Dimension Key (for Order Date)
    fact_table = fact_table.merge(date_dim.rename(columns={'Date': 'Order Date'}), on='Order Date', how='left')
    # Selecting Fact Table Columns
    fact_table = fact_table[[
        'Customer_Key', 'Product_Key', 'Date_Key',  # Foreign keys
        'Sales', 'Quantity', 'Discount', 'Profit',  # Metrics
        'Ship Mode', 'Region', 'City', 'Country'   # Additional attributes
    ]]
    return fact_table

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "superstore/samplesuperstore.csv", encoding='UTF8')
    data = df[ ['Order Date', 'Ship Date', 'Ship Mode',
                'Customer Name', 'Segment', 'Country', 'City', 'State',
                'Postal Code', 'Region',  'Category', 'Sub-Category',
                'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit'] ]
    
    customer_dim, product_dim, date_dim = create_dimension_tables(data)
    fact_table = create_fact_table(data, customer_dim, product_dim, date_dim)
    print(fact_table.head())
    print(customer_dim.head())
