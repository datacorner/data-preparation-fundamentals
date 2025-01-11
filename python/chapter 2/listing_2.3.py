import pandas as pd
import matplotlib.pyplot as plt

def initialize():
    """ Read the source file (Titanic disaster) and provide a dataframe

    Returns:
        dataframe: titanic dataset
    """
    # read the CSV file
    df = pd.read_csv("../Titanic disaster/train.csv")
    # survived=0 means the passenger died, survived=1 means he survived, let's make it more clear in the dataset:
    df['SurvivedProba'] = df['Survived']
    df['SurvivedLabel'] = df['Survived'].map({1: 'alive' , 0: 'dead'})
    return df

def analyzeByAge(_df):
    """Analyze the Titanic dataset by Age

    Args:
        _df (dataframe): titanic dataset
    """
    print(df["Age"].isnull().sum())
    # Only keep the rows with an age
    with_age = df.dropna(subset=['Age'])

    # Calculate some stats
    titanic_age_mean = with_age["Age"].mean()
    titanic_age_median = with_age["Age"].median()
    titanic_age_q1 = with_age['Age'].quantile(0.25)
    titanic_age_q3 = with_age['Age'].quantile(0.75)
    
    # Display Passenger count per age
    plt.figure(figsize=(14, 4))
    plt.hist(with_age["Age"], bins=20, edgecolor='black', alpha=0.7)
    plt.axvline(titanic_age_q1, color='red', linestyle='--', label='1st quartile (25%)')
    plt.axvline(titanic_age_median, color='green', linestyle='-', label='Median (50%)')
    plt.axvline(titanic_age_mean, color='orange', linestyle='-', label='Mean')
    plt.axvline(titanic_age_q3, color='red', linestyle='--', label='3rd quartile (75%)')
    plt.title('Number of Titanic passengers by age', fontsize=16)
    plt.xlabel('Passenger Age', fontsize=14)
    plt.ylabel('Number of passengers', fontsize=14)
    plt.show()

if __name__ == "__main__":
    df = initialize()
    analyzeByAge(df)