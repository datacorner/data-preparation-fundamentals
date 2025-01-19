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

if __name__ == "__main__":
    df = initialize()

    # Imputing by using Forward and backforward techniques
    print("Original 'Age' column with missing values:\n", df['Age']) #A
    df['age_ffill'] = df['Age'].fillna(method='ffill') #B
    print("\n'Age' column after forward filling:\n", df['age_ffill'])
    df['age_bfill'] = df['Age'].fillna(method='bfill') #C
    print("\n'Age' column after backward filling:\n", df['age_bfill'])

    print (df)