import pandas as pd
import matplotlib.pyplot as plt

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
    df = pd.read_csv("../data/superstore/samplesuperstore.csv", encoding='UTF8')

    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    customer_orders = df.groupby('Customer ID').agg({
        'Order ID': 'count',           
        'Sales': 'sum',                
        'Profit': 'sum',               
        'Order Date': ['min', 'max']   
    }).reset_index()

    customer_orders.columns = [
        'Customer ID', 'Total Orders', 'Total Sales',
        'Total Profit', 'First Purchase', 'Last Purchase'
    ]

    customer_orders['Customer Tenure Days'] = (
        customer_orders['Last Purchase'] - customer_orders['First Purchase']
    ).dt.days

    customer_orders['Funnel Stage'] =  customer_orders['Total Orders'].apply(classify_funnel_stage) #A
    funnel_distribution = customer_orders['Funnel Stage'].value_counts(normalize=True) * 100 #B

    plt.figure(figsize=(10, 6))
    funnel_distribution.plot(kind='bar')
    plt.title('Customer Purchase Funnel Distribution')
    plt.xlabel('Funnel Stage')
    plt.ylabel('Percentage of Customers')
    plt.tight_layout()
    plt.show()
