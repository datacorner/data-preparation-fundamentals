import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

def cohort_step_1(df):
    # Convert 'Order Date' to datetime format
    df['Order Date'] = pd.to_datetime(df['Order Date'], 
                                    format='%m/%d/%Y') #A
    data = df[df['Order Date'].dt.year == 2017]
    # Create Cohort Group (First Purchase Month by customer)
    customer_first_purchase = data.groupby('Customer ID')['Order Date'].min()
    data['Cohort_Group'] = data['Customer ID'].map(customer_first_purchase) #B
    # Extract Cohort Month and Order Month
    data['Cohort_Month'] = data['Cohort_Group'].dt.to_period('M')  #C
    data['Order_Month'] = data['Order Date'].dt.to_period('M')     
    data['Months_Since_First_Purchase'] = (data['Order_Month'] - data['Cohort_Month']).apply(lambda x: x.n) #D
    return data

def cohort_step_2(data):
    # Cohort Retention Calculation
    return data.groupby(['Cohort_Month',
                                    'Months_Since_First_Purchase']).agg({
                                        'Customer ID': 'nunique'
    }).reset_index()

def cohort_step_3(df):
    cohort_group_size = df.groupby('Cohort_Month')['Customer ID'].first()
    df['Retention_Rate'] = df.apply (
                    lambda x: x['Customer ID'] /  cohort_group_size[x['Cohort_Month']] *  100,
                    axis=1
                    )
    return df

if __name__ == "__main__":
    df = pd.read_csv("../data/superstore/samplesuperstore.csv", encoding='UTF8')
    ch1 = cohort_step_1(df) 
    ch2 = cohort_step_2(ch1)
    ch3 = cohort_step_3(ch2)

    # Step 1: Pivot the DataFrame
    cohort_pivot = ch3.pivot(
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