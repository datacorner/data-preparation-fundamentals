import pandas as pd

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C


def initialize():
    """ Read the source file (Titanic disaster) and provide a dataframe

    Returns:
        dataframe: titanic dataset
    """
    # read the CSV file
    df = pd.read_csv(C.DATASET_FOLDER + "titanic/train.csv")
    # survived=0 means the passenger died, survived=1 means he survived, let's make it more clear in the dataset:
    df['SurvivedProba'] = df['Survived']
    df['SurvivedLabel'] = df['Survived'].map({1: 'alive' , 0: 'dead'})
    return df

def check_same_fare_for_tickets(df):
    # Group by Ticket and get unique fares for each ticket
    ticket_fares = df.groupby('Ticket')['Fare'].unique().reset_index()
    # Check if all fares for each ticket are the same
    ticket_fares['SameFare'] = ticket_fares['Fare'].apply(lambda x: len(set(x)) == 1)
    # Merge this information back to the original dataframe
    df_result = df.merge(ticket_fares[['Ticket', 'SameFare']], on='Ticket', how='left')
    return df_result

if __name__ == "__main__":
    df = initialize()
    df_same_fare = check_same_fare_for_tickets(df)
    print("\nPercentage of tickets with same fare:")
    print(df_same_fare['SameFare'].value_counts(normalize=True) * 100)
