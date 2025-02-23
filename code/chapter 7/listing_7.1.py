import pandas as pd

def create_dimension_tables(df):
    """Create dimension tables
    Args:
        df (pandas.DataFrame): dataset
    Returns:
        pandas.DataFrame[]: list of dimension tables as dataframe
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

if __name__ == "__main__":
    df = pd.read_csv("../data/superstore/samplesuperstore.csv", encoding='UTF8')
    data = df[ ['Order Date', 'Ship Date', 'Ship Mode',
                'Customer Name', 'Segment', 'Country', 'City', 'State',
                'Postal Code', 'Region',  'Category', 'Sub-Category',
                'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit'] ]
    
    customer_dim, product_dim, date_dim = create_dimension_tables(data)
    print(customer_dim.head())
