import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
    
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

    # Using linear interpolation to impute values (MICE)
    imputer = IterativeImputer()
    # Selecting relevant columns for imputation
    # It's a good practice to include other numeric columns for a better imputation
    columns_for_imputation = ['Age', 'SibSp', 'Parch', 'Fare']
    df_subset = df[columns_for_imputation]
    # Perform imputation
    df_imputed = imputer.fit_transform(df_subset)
    # Replace the original columns with imputed values
    df[columns_for_imputation] = df_imputed
    
    print (df)