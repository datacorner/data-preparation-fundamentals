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
    # Dropping column instead of rows (column-wide deletion)
    missing_percentage = df.isnull().sum() / len(df) * 100
    columns_to_drop = missing_percentage[missing_percentage > 50].index
    titanic_reduced = df.drop(columns=columns_to_drop)
    print ("columns dropped:", columns_to_drop)

