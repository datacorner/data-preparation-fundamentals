import pandas as pd

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

def create_time_features(series):
    """
    Generates advanced time-based features for a given time series.
    This function computes several features based on the input time series:
    1. Rolling 7-day and 30-day moving averages.
    2. Exponentially Weighted Moving Average (EWMA) with a span of 30 days.
    3. Year-over-Year percentage change.
    Parameters:
        series (pandas.Series): A time series data to generate features from.
    Returns:
        pandas.DataFrame: A DataFrame containing the computed time-based features.
    """
    return pd.DataFrame({
        # Rolling window means. calculates the 7-day and 30-day moving average of the time series data
        'Rolling_7D_Mean': series.rolling(window=7).mean(),
        'Rolling_30D_Mean': series.rolling(window=30).mean(),
        # Exponential Weighted Moving Average
        'Exponential_Weighted_Mean': series.ewm(span=30).mean(),
        # Year-over-Year Percentage Change
        'Year_Over_Year_Change': series.pct_change(periods=365) * 100
    })

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "superstore/samplesuperstore.csv", encoding='UTF8')
    
    # Convert Order Date to datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    # Display date range to confirm conversion
    print("Date Range:", df['Order Date'].min(), "to", df['Order Date'].max())

    daily_sales = df.groupby('Order Date').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count'
    }).rename(columns={'Order ID': 'Transaction_Count'})
    
    # Apply time features to Sales column
    time_features = create_time_features(daily_sales['Sales'])

    # Add these features to daily_sales
    daily_sales = pd.concat([daily_sales, time_features], axis=1)

    # Display the updated dataframe
    print(daily_sales.head())