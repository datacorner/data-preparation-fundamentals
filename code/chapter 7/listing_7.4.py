import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../data/superstore/samplesuperstore.csv", encoding='UTF8')

    df['Profit_Margin'] = df['Profit'] / df['Sales'] * 100
    customer_ltv = df.groupby('Customer ID').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count'
    }).rename(columns={'Order ID': 'Purchase_Frequency'})

    customer_ltv['Profit_Margin'] = (df.groupby('Customer ID')['Profit_Margin']
                                    .mean().fillna(0))  # A

    customer_ltv['Customer_LTV'] = (
        customer_ltv['Sales'] *
        (1 + customer_ltv['Profit_Margin'] / 100) *
        customer_ltv['Purchase_Frequency']
    ) #B
    print(customer_ltv.head())