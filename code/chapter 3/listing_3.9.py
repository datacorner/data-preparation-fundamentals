import pandas as pd
from sklearn.impute import KNNImputer

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

def display_missing_values(df):
    """ This function calculates and displays the percentage of missing values for 
        each column in the given DataFrame. It also prints the total number of rows 
        and columns in the dataset.
    Parameters:
        df (pd.DataFrame): The input DataFrame to analyze.
    Returns:
        None: The function prints the following to the console:
            - The percentage of missing values for each column, rounded to one decimal place.
            - The total number of rows and columns in the DataFrame.
    """
    missing_percentage = df.isnull().sum() / len(df) * 100
    print("% of Missing values:")
    print(missing_percentage.apply(lambda x: f"{x:.1f}"))
    print("Rows: {} | Columns: {}".format(df.shape[0], df.shape[1]))

if __name__ == "__main__":
    df = initialize()

    # Create a KNNImputer instance with n_neighbors set to 3
    imputer = KNNImputer(n_neighbors=3)
    # Impute missing values in the 'Age' column
    df['Age'] = imputer.fit_transform(df[['Age']])

    display_missing_values(df)