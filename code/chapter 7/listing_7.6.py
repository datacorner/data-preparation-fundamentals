import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../data/superstore/samplesuperstore.csv", encoding='UTF8')
    
    # Convert Order Date to datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    # Display date range to confirm conversion
    print("Date Range:", df['Order Date'].min(), "to", df['Order Date'].max())

    daily_sales = df.groupby('Order Date').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count'
    }).rename(columns={'Order ID': 'Transaction_Count'})

    print(daily_sales.head())