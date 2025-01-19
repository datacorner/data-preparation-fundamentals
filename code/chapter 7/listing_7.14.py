import pandas as pd
import matplotlib.pyplot as plt

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

def classify_funnel_stage(orders):
    """
    Classifies a customer into different funnel stages based on their order count.
    This function categorizes customers based on the number of orders they have made:
    1. 'One-Time Buyer' for customers with 1 order.
    2. 'Repeat Buyer' for customers with 2 orders.
    3. 'Frequent Buyer' for customers with 3 to 4 orders.
    4. 'Loyal Customer' for customers with more than 4 orders.
    Parameters:
        orders (int): The number of orders a customer has placed.
    Returns:
        str: The customer classification as a funnel stage ('One-Time Buyer', 'Repeat Buyer', 'Frequent Buyer', or 'Loyal Customer').
    """
    if orders == 1:
        return 'One-Time Buyer'
    elif orders == 2:
        return 'Repeat Buyer'
    elif orders <= 4:
        return 'Frequent Buyer'
    else:
        return 'Loyal Customer'

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "superstore/samplesuperstore.csv", encoding='UTF8')

    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

    # Group by Customer ID to get unique customer metrics
    customer_orders = df.groupby('Customer ID').agg({
        'Order ID': 'count',           # Total number of orders
        'Sales': 'sum',                # Total sales per customer
        'Profit': 'sum',               # Total profit per customer
        'Order Date': ['min', 'max']   # First and last purchase dates
    }).reset_index()

    # Rename columns for clarity
    customer_orders.columns = [
        'Customer ID', 'Total Orders', 'Total Sales',
        'Total Profit', 'First Purchase', 'Last Purchase'
    ]

    # Calculate customer tenure
    customer_orders['Customer Tenure Days'] = (
        customer_orders['Last Purchase'] - customer_orders['First Purchase']
    ).dt.days

    customer_orders['Funnel Stage'] =  customer_orders['Total Orders'].apply(classify_funnel_stage) 
    funnel_distribution = customer_orders['Funnel Stage'].value_counts(normalize=True) * 100 

    plt.figure(figsize=(10, 6))
    funnel_distribution.plot(kind='bar')
    plt.title('Customer Purchase Funnel Distribution')
    plt.xlabel('Funnel Stage')
    plt.ylabel('Percentage of Customers')
    plt.tight_layout()
    plt.show()
