import pandas as pd
from scipy import stats
import numpy as np

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

def zscore_method(data, threshold=3):
    z_scores = np.abs(stats.zscore(data))
    outliers = data[z_scores > threshold]
    return outliers

if __name__ == "__main__":
    df = initialize()
    distrib = df['Age'].dropna()

    # Using the Z-Score method on ages
    zscore_outliers = zscore_method(distrib)
    
    print("Number of outliers", len(zscore_outliers))
    print(', '.join(map(str, zscore_outliers.values)))