import pandas as pd

def check_same_fare_for_tickets(df):
    # Group by Ticket and get unique fares for each ticket
    ticket_fares = df.groupby('Ticket')['Fare'].unique().reset_index()
    # Check if all fares for each ticket are the same
    ticket_fares['SameFare'] = ticket_fares['Fare'].apply(lambda x: len(set(x)) == 1)
    # Merge this information back to the original dataframe
    df_result = df.merge(ticket_fares[['Ticket', 
                                    'SameFare']], on='Ticket', how='left')
    return df_result

if __name__ == "__main__":
    # read the CSV file
    df = pd.read_csv("../data/titanic/train.csv")
    df_same_fare = check_same_fare_for_tickets(df)
    print("\nPercentage of tickets with same fare:")
    print(df_same_fare['SameFare'].value_counts(normalize=True) * 100)
