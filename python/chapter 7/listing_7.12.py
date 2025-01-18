import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

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

    cohort_group_size = cohort_retention.groupby('Cohort_Month')['Customer ID'].first()
    cohort_retention['Retention_Rate'] = cohort_retention.apply (
                    lambda x: x['Customer ID'] /  cohort_group_size[x['Cohort_Month']] *  100,
                    axis=1
                    )

    # Step 1: Pivot the DataFrame
    cohort_pivot = cohort_retention.pivot(
        index='Cohort_Month',
        columns='Months_Since_First_Purchase',
        values='Retention_Rate'
    )
    
    # Plot the heatmap
    month_names = [calendar.month_name[i+1 % 12] for i in range(len(cohort_pivot.columns))]
    plt.figure(figsize=(8, 5))
    sns.heatmap(
        cohort_pivot,
        annot=True,
        fmt='.0f',  # Show as integers (e.g., percentages without decimals)
        cmap='coolwarm',
        cbar_kws={'label': 'Retention Rate (%)'},
        xticklabels=month_names  # Set the x-axis labels as month names
    )
    plt.title('Customer Retention by Monthly Cohort', fontsize=16)
    plt.xlabel('Months Since First Purchase', fontsize=12)
    plt.ylabel('Cohort Month', fontsize=12)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()