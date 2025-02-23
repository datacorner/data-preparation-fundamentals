import pandas as pd

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

if __name__ == "__main__":
    df = pd.read_csv("../data/superstore/samplesuperstore.csv", encoding='UTF8')
    ch1 = cohort_step_1(df) 
    ch2 = cohort_step_2(ch1)

    print(ch2.head())