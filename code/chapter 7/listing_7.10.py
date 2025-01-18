import pandas as pd

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "superstore/samplesuperstore.csv", encoding='UTF8')

    # Convert 'Order Date' to datetime format
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
    data = df[df['Order Date'].dt.year == 2017]
    # Create Cohort Group (First Purchase Month by customer)
    customer_first_purchase = data.groupby('Customer ID')['Order Date'].min()
    data['Cohort_Group'] = data['Customer ID'].map(customer_first_purchase)
    # Extract Cohort Month and Order Month
    data['Cohort_Month'] = data['Cohort_Group'].dt.to_period('M')  # Converts to Period (Month)
    data['Order_Month'] = data['Order Date'].dt.to_period('M')     # Converts to Period (Month)

    # we calculate the number of months since the first purchase, and the retention duration
    data['Months_Since_First_Purchase'] = (data['Order_Month'] - data['Cohort_Month']).apply(lambda x: x.n)

    # Cohort Retention Calculation
    cohort_retention = data.groupby(['Cohort_Month',
                                    'Months_Since_First_Purchase']).agg({
                                        'Customer ID': 'nunique'
    }).reset_index()

    print(cohort_retention.head())