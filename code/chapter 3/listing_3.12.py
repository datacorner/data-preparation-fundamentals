import pandas as pd
from scipy import stats

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

if __name__ == "__main__":
    df = initialize()
    distrib = df['Age'].dropna()

    # Using the Shapiro-Wilk test on ages
    statistic, p_value = stats.shapiro(distrib)
    print(f"Shapiro-Wilk test results:")
    print(f"Statistic: {statistic:.6f}")
    print(f"p-value: {p_value:.6f}")
    if p_value > 0.05:
        print("The age distribution is likely normal (fail to reject H0)")
    else:
        print("The age distribution is likely not normal (reject H0)")
