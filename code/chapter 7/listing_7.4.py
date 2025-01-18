import pandas as pd

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "superstore/samplesuperstore.csv", encoding='UTF8')

    df['Profit_Margin'] = df['Profit'] / df['Sales'] * 100
    customer_ltv = df.groupby('Customer ID').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count'
    }).rename(columns={'Order ID': 'Purchase_Frequency'})

    # Calculate the average Profit Margin per customer
    customer_ltv['Profit_Margin'] = (df.groupby('Customer ID')['Profit_Margin']
                                    .mean().fillna(0))  # Handle potential NaN values

    # Calculate Customer Lifetime Value (LTV)
    customer_ltv['Customer_LTV'] = (
        customer_ltv['Sales'] *
        (1 + customer_ltv['Profit_Margin'] / 100) *
        customer_ltv['Purchase_Frequency']
    )
    print(customer_ltv.head())